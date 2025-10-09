// generated from rosidl_generator_cpp/resource/rosidl_generator_cpp__visibility_control.hpp.in
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_ACTION_DRIVE__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
#define TURTLEBOT_ACTION_DRIVE__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_CPP_EXPORT_turtlebot_action_drive __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_CPP_IMPORT_turtlebot_action_drive __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_CPP_EXPORT_turtlebot_action_drive __declspec(dllexport)
    #define ROSIDL_GENERATOR_CPP_IMPORT_turtlebot_action_drive __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_CPP_BUILDING_DLL_turtlebot_action_drive
    #define ROSIDL_GENERATOR_CPP_PUBLIC_turtlebot_action_drive ROSIDL_GENERATOR_CPP_EXPORT_turtlebot_action_drive
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_turtlebot_action_drive ROSIDL_GENERATOR_CPP_IMPORT_turtlebot_action_drive
  #endif
#else
  #define ROSIDL_GENERATOR_CPP_EXPORT_turtlebot_action_drive __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_CPP_IMPORT_turtlebot_action_drive
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_CPP_PUBLIC_turtlebot_action_drive __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_turtlebot_action_drive
  #endif
#endif

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT_ACTION_DRIVE__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
