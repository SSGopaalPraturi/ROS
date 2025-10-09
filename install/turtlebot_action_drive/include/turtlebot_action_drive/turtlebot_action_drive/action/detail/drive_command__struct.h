// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtlebot_action_drive:action/DriveCommand.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "turtlebot_action_drive/action/drive_command.h"


#ifndef TURTLEBOT_ACTION_DRIVE__ACTION__DETAIL__DRIVE_COMMAND__STRUCT_H_
#define TURTLEBOT_ACTION_DRIVE__ACTION__DETAIL__DRIVE_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_Goal
{
  /// Distance to move in meters (0 if turning)
  float distance;
  /// Angle to turn in radians (0 if moving)
  float angle;
} turtlebot_action_drive__action__DriveCommand_Goal;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_Goal.
typedef struct turtlebot_action_drive__action__DriveCommand_Goal__Sequence
{
  turtlebot_action_drive__action__DriveCommand_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_Goal__Sequence;

// Constants defined in the message

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_Result
{
  uint8_t structure_needs_at_least_one_member;
} turtlebot_action_drive__action__DriveCommand_Result;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_Result.
typedef struct turtlebot_action_drive__action__DriveCommand_Result__Sequence
{
  turtlebot_action_drive__action__DriveCommand_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_Result__Sequence;

// Constants defined in the message

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_Feedback
{
  uint8_t structure_needs_at_least_one_member;
} turtlebot_action_drive__action__DriveCommand_Feedback;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_Feedback.
typedef struct turtlebot_action_drive__action__DriveCommand_Feedback__Sequence
{
  turtlebot_action_drive__action__DriveCommand_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_Feedback__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "turtlebot_action_drive/action/detail/drive_command__struct.h"

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  turtlebot_action_drive__action__DriveCommand_Goal goal;
} turtlebot_action_drive__action__DriveCommand_SendGoal_Request;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_SendGoal_Request.
typedef struct turtlebot_action_drive__action__DriveCommand_SendGoal_Request__Sequence
{
  turtlebot_action_drive__action__DriveCommand_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_SendGoal_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} turtlebot_action_drive__action__DriveCommand_SendGoal_Response;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_SendGoal_Response.
typedef struct turtlebot_action_drive__action__DriveCommand_SendGoal_Response__Sequence
{
  turtlebot_action_drive__action__DriveCommand_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_SendGoal_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  turtlebot_action_drive__action__DriveCommand_SendGoal_Event__request__MAX_SIZE = 1
};
// response
enum
{
  turtlebot_action_drive__action__DriveCommand_SendGoal_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_SendGoal_Event
{
  service_msgs__msg__ServiceEventInfo info;
  turtlebot_action_drive__action__DriveCommand_SendGoal_Request__Sequence request;
  turtlebot_action_drive__action__DriveCommand_SendGoal_Response__Sequence response;
} turtlebot_action_drive__action__DriveCommand_SendGoal_Event;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_SendGoal_Event.
typedef struct turtlebot_action_drive__action__DriveCommand_SendGoal_Event__Sequence
{
  turtlebot_action_drive__action__DriveCommand_SendGoal_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_SendGoal_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} turtlebot_action_drive__action__DriveCommand_GetResult_Request;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_GetResult_Request.
typedef struct turtlebot_action_drive__action__DriveCommand_GetResult_Request__Sequence
{
  turtlebot_action_drive__action__DriveCommand_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_GetResult_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "turtlebot_action_drive/action/detail/drive_command__struct.h"

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_GetResult_Response
{
  int8_t status;
  turtlebot_action_drive__action__DriveCommand_Result result;
} turtlebot_action_drive__action__DriveCommand_GetResult_Response;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_GetResult_Response.
typedef struct turtlebot_action_drive__action__DriveCommand_GetResult_Response__Sequence
{
  turtlebot_action_drive__action__DriveCommand_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_GetResult_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  turtlebot_action_drive__action__DriveCommand_GetResult_Event__request__MAX_SIZE = 1
};
// response
enum
{
  turtlebot_action_drive__action__DriveCommand_GetResult_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_GetResult_Event
{
  service_msgs__msg__ServiceEventInfo info;
  turtlebot_action_drive__action__DriveCommand_GetResult_Request__Sequence request;
  turtlebot_action_drive__action__DriveCommand_GetResult_Response__Sequence response;
} turtlebot_action_drive__action__DriveCommand_GetResult_Event;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_GetResult_Event.
typedef struct turtlebot_action_drive__action__DriveCommand_GetResult_Event__Sequence
{
  turtlebot_action_drive__action__DriveCommand_GetResult_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_GetResult_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "turtlebot_action_drive/action/detail/drive_command__struct.h"

/// Struct defined in action/DriveCommand in the package turtlebot_action_drive.
typedef struct turtlebot_action_drive__action__DriveCommand_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  turtlebot_action_drive__action__DriveCommand_Feedback feedback;
} turtlebot_action_drive__action__DriveCommand_FeedbackMessage;

// Struct for a sequence of turtlebot_action_drive__action__DriveCommand_FeedbackMessage.
typedef struct turtlebot_action_drive__action__DriveCommand_FeedbackMessage__Sequence
{
  turtlebot_action_drive__action__DriveCommand_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_action_drive__action__DriveCommand_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT_ACTION_DRIVE__ACTION__DETAIL__DRIVE_COMMAND__STRUCT_H_
