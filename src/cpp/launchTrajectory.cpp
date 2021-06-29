// -*- mode:C++; tab-width:4; c-basic-offset:4; indent-tabs-mode:nil -*-

/**
 * @ingroup teo_blender_models_src
 * @defgroup launchTrajectory launchTrajectory
 * @brief This application connects to the remote controlboard devices of the robot, read a csv file and sends position direct commands.
 */

#include <yarp/os/Network.h>
#include <yarp/os/Property.h>
#include <yarp/os/ResourceFinder.h>
#include <yarp/os/Time.h>

#include <yarp/dev/IControlMode.h>
#include <yarp/dev/IEncoders.h>
#include <yarp/dev/IPositionControl.h>
#include <yarp/dev/IPositionDirect.h>
#include <yarp/dev/IRemoteVariables.h>
#include <yarp/dev/PolyDriver.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>

#define DEFAULT_ROBOT "/teo"
#define DEFAULT_POSD_PERIOD_MS 50
#define DEFAULT_IP_MODE "pt"

int main(int argc, char *argv[])
{
    yarp::os::ResourceFinder rf;
    rf.configure(argc, argv);

    std::string robot = rf.check("robot",yarp::os::Value(DEFAULT_ROBOT),"name of robot to be used").asString();
    std::string csvPath = rf.check("csv",yarp::os::Value(DEFAULT_ROBOT),"path of csv file to be used").asString();
    int period = rf.check("period", yarp::os::Value(DEFAULT_POSD_PERIOD_MS), "posd command period [ms]").asInt32();
    bool batch = rf.check("batch",  "stream interpolation data in batches");
    std::string ipMode = rf.check("ipMode", yarp::os::Value(DEFAULT_IP_MODE), "linear interpolation mode [pt|pvt]").asString();

    if(!rf.check("csv"))
    {
        printf("[error] csv parameter not found. Please, indicate --csv file.csv\n");
        return false;
    }

    if (period <= 0)
    {
        printf("[error] Illegal period: %d.\n", period);
        return false;
    }

    if (ipMode != "pt" && ipMode != "pvt")
    {
        printf("[error] Illegal ipMode: %s.\n", ipMode.c_str());
        return false;
    }

    yarp::os::Network yarp;

    if (!yarp::os::Network::checkNetwork())
    {
        printf("[error] Please start a yarp name server first.\n");
        return 1;
    }

    // ------ LEFT ARM -------
    yarp::dev::IControlMode * lamode;
    yarp::dev::IEncoders * laencs;
    yarp::dev::IPositionControl * lapos;
    yarp::dev::IPositionDirect * laposd;
    yarp::dev::IRemoteVariables * lavar;


    yarp::os::Property laoptions;
    laoptions.put("device","remote_controlboard");
    laoptions.put("writeStrict", "on");
    laoptions.put("remote",robot+"/leftArm");
    laoptions.put("local","/test"+robot+"/leftArm");

    yarp::dev::PolyDriver ladev(laoptions);

    ladev.open(laoptions);
    if(!ladev.isValid()) {
      printf("[error] Robot device not available: left-arm\n");
      ladev.close();
      yarp::os::Network::fini();
      return false;
    }

    bool laok = true;

    laok &= ladev.view(lamode);
    laok &= ladev.view(laencs);
    laok &= ladev.view(lapos);
    laok &= ladev.view(laposd);
    laok &= !batch || ladev.view(lavar);

    if (!ladev.isValid())
    {
      printf("[error] Remote device not available: left-arm\n");
      return 1;
    }

    if (!laok)
    {
        printf("[error] Problems acquiring robot interfaces: left-arm\n");
        return 1;
    }


    // ------ RIGHT ARM -------
    yarp::dev::IControlMode * ramode;
    yarp::dev::IEncoders * raencs;
    yarp::dev::IPositionControl * rapos;
    yarp::dev::IPositionDirect * raposd;
    yarp::dev::IRemoteVariables * ravar;


    yarp::os::Property raoptions;
    raoptions.put("device","remote_controlboard");
    raoptions.put("writeStrict", "on");
    raoptions.put("remote",robot+"/rightArm");
    raoptions.put("local","/test"+robot+"/rightArm");

    yarp::dev::PolyDriver radev(raoptions);

    radev.open(raoptions);
    if(!radev.isValid()) {
      printf("[error] Robot device not available: right-arm\n");
      radev.close();
      yarp::os::Network::fini();
      return false;
    }

    bool raok = true;

    raok &= radev.view(ramode);
    raok &= radev.view(raencs);
    raok &= radev.view(rapos);
    raok &= radev.view(raposd);
    raok &= !batch || radev.view(ravar);

    if (!radev.isValid())
    {
      printf("[error] Remote device not available: right-arm\n");
      return 1;
    }

    if (!raok)
    {
        printf("[error] Problems acquiring robot interfaces: right-arm\n");
        return 1;
    }

    // ------ TRUNK -------
    yarp::dev::IControlMode * trmode;
    yarp::dev::IEncoders * trencs;
    yarp::dev::IPositionControl * trpos;
    yarp::dev::IPositionDirect * trposd;
    yarp::dev::IRemoteVariables * trvar;


    yarp::os::Property troptions;
    troptions.put("device","remote_controlboard");
    troptions.put("writeStrict", "on");
    troptions.put("remote",robot+"/trunk");
    troptions.put("local","/test"+robot+"/trunk");

    yarp::dev::PolyDriver trdev(troptions);

    trdev.open(troptions);
    if(!trdev.isValid()) {
      printf("[error] Robot device not available: trunk\n");
      trdev.close();
      yarp::os::Network::fini();
      return false;
    }

    bool trok = true;

    trok &= trdev.view(trmode);
    trok &= trdev.view(trencs);
    trok &= trdev.view(trpos);
    trok &= trdev.view(trposd);
    trok &= !batch || trdev.view(trvar);

    if (!trdev.isValid())
    {
      printf("[error] Remote device not available: trunk\n");
      return 1;
    }

    if (!raok)
    {
        printf("[error] Problems acquiring robot interfaces: trunk\n");
        return 1;
    }


    if (batch)
    {
        yarp::os::Property dict {{"enable", yarp::os::Value(true)},
                                 {"mode", yarp::os::Value(ipMode)},
                                 {"periodMs", yarp::os::Value(period)}};

        yarp::os::Value v;
        v.asList()->addString("linInterp");
        v.asList()->addList().fromString(dict.toString());

        if (!lavar->setRemoteVariable("all", {v})
         || !ravar->setRemoteVariable("all", {v})
         || !trvar->setRemoteVariable("all", {v}))

        {
            printf("[error] Unable to set linear interpolation mode.\n");
            return 1;
        }
    }

    int lajoints;
    laencs->getAxes(&lajoints);
    std::vector<int> lamodes(lajoints,VOCAB_CM_POSITION_DIRECT);
    lamode->setControlModes(lamodes.data());

    int rajoints;
    raencs->getAxes(&rajoints);
    std::vector<int> ramodes(rajoints,VOCAB_CM_POSITION_DIRECT);
    ramode->setControlModes(ramodes.data());

    int trjoints;
    trencs->getAxes(&trjoints);
    std::vector<int> trmodes(trjoints,VOCAB_CM_POSITION_DIRECT);
    trmode->setControlModes(trmodes.data());

    // Read CSV file and move
    std::ifstream ifstr;
    std::vector<double> csvrow, lapose, rapose, trpose;
    ifstr.open(csvPath,std::ios::in);

    for (std::string line; std::getline(ifstr, line); )
    {
        std::stringstream rec(line);

        for (std::string data; std::getline(rec, data, ','); )
        {
            csvrow.push_back( std::stod(data));
        }

        for(int n=0; n<csvrow.size(); n++)
            printf("%f ", csvrow[n]);
        printf("\n");

        copy ( csvrow.begin(),    csvrow.begin()+ 6, std::back_inserter(lapose) );
        copy ( csvrow.begin()+6,  csvrow.begin()+12, std::back_inserter(rapose) );
        copy ( csvrow.begin()+12, csvrow.begin()+14, std::back_inserter(trpose) );

        laposd->setPositions(lapose.data());
        raposd->setPositions(rapose.data());
        trposd->setPositions(trpose.data());

        if(!batch)
        {
            yarp::os::Time::delay(period * 0.001);
        }

        csvrow.clear();
        lapose.clear();
        rapose.clear();
        trpose.clear();
    }

    printf("end\n");

    return 0;
}
