cmake_minimum_required(VERSION 3.8)
project(turtlebot_action_drive)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(action_msgs REQUIRED)

# Generate the action interface
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/DriveCommand.action"
  DEPENDENCIES action_msgs
)

# Install Python scripts directly
install(PROGRAMS
  turtlebot_action_drive/executive_node.py
  turtlebot_action_drive/driving_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/launch")
  install(DIRECTORY
    launch
    DESTINATION share/${PROJECT_NAME}/
  )
endif()

ament_export_dependencies(rosidl_default_runtime)

ament_package()