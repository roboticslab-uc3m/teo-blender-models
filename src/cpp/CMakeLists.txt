cmake_minimum_required(VERSION 3.12 FATAL_ERROR)

project(launchTrajectory LANGUAGES CXX)

find_package(YARP 3.2 REQUIRED COMPONENTS os dev)

add_executable(launchTrajectory launchTrajectory.cpp)

target_link_libraries(launchTrajectory YARP::YARP_os
                                            YARP::YARP_init
                                            YARP::YARP_dev)
