// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtlebot_action_drive:action/DriveCommand.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "turtlebot_action_drive/action/drive_command.hpp"


#ifndef TURTLEBOT_ACTION_DRIVE__ACTION__DETAIL__DRIVE_COMMAND__BUILDER_HPP_
#define TURTLEBOT_ACTION_DRIVE__ACTION__DETAIL__DRIVE_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtlebot_action_drive/action/detail/drive_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_Goal_angle
{
public:
  explicit Init_DriveCommand_Goal_angle(::turtlebot_action_drive::action::DriveCommand_Goal & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_Goal angle(::turtlebot_action_drive::action::DriveCommand_Goal::_angle_type arg)
  {
    msg_.angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_Goal msg_;
};

class Init_DriveCommand_Goal_distance
{
public:
  Init_DriveCommand_Goal_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_Goal_angle distance(::turtlebot_action_drive::action::DriveCommand_Goal::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_DriveCommand_Goal_angle(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_Goal>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_Goal_distance();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{


}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_Result>()
{
  return ::turtlebot_action_drive::action::DriveCommand_Result(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{


}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_Feedback>()
{
  return ::turtlebot_action_drive::action::DriveCommand_Feedback(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_SendGoal_Request_goal
{
public:
  explicit Init_DriveCommand_SendGoal_Request_goal(::turtlebot_action_drive::action::DriveCommand_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Request goal(::turtlebot_action_drive::action::DriveCommand_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Request msg_;
};

class Init_DriveCommand_SendGoal_Request_goal_id
{
public:
  Init_DriveCommand_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_SendGoal_Request_goal goal_id(::turtlebot_action_drive::action::DriveCommand_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_DriveCommand_SendGoal_Request_goal(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_SendGoal_Request>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_SendGoal_Request_goal_id();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_SendGoal_Response_stamp
{
public:
  explicit Init_DriveCommand_SendGoal_Response_stamp(::turtlebot_action_drive::action::DriveCommand_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Response stamp(::turtlebot_action_drive::action::DriveCommand_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Response msg_;
};

class Init_DriveCommand_SendGoal_Response_accepted
{
public:
  Init_DriveCommand_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_SendGoal_Response_stamp accepted(::turtlebot_action_drive::action::DriveCommand_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_DriveCommand_SendGoal_Response_stamp(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_SendGoal_Response>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_SendGoal_Response_accepted();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_SendGoal_Event_response
{
public:
  explicit Init_DriveCommand_SendGoal_Event_response(::turtlebot_action_drive::action::DriveCommand_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Event response(::turtlebot_action_drive::action::DriveCommand_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Event msg_;
};

class Init_DriveCommand_SendGoal_Event_request
{
public:
  explicit Init_DriveCommand_SendGoal_Event_request(::turtlebot_action_drive::action::DriveCommand_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_DriveCommand_SendGoal_Event_response request(::turtlebot_action_drive::action::DriveCommand_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_DriveCommand_SendGoal_Event_response(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Event msg_;
};

class Init_DriveCommand_SendGoal_Event_info
{
public:
  Init_DriveCommand_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_SendGoal_Event_request info(::turtlebot_action_drive::action::DriveCommand_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_DriveCommand_SendGoal_Event_request(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_SendGoal_Event>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_SendGoal_Event_info();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_GetResult_Request_goal_id
{
public:
  Init_DriveCommand_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Request goal_id(::turtlebot_action_drive::action::DriveCommand_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_GetResult_Request>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_GetResult_Request_goal_id();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_GetResult_Response_result
{
public:
  explicit Init_DriveCommand_GetResult_Response_result(::turtlebot_action_drive::action::DriveCommand_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Response result(::turtlebot_action_drive::action::DriveCommand_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Response msg_;
};

class Init_DriveCommand_GetResult_Response_status
{
public:
  Init_DriveCommand_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_GetResult_Response_result status(::turtlebot_action_drive::action::DriveCommand_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_DriveCommand_GetResult_Response_result(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_GetResult_Response>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_GetResult_Response_status();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_GetResult_Event_response
{
public:
  explicit Init_DriveCommand_GetResult_Event_response(::turtlebot_action_drive::action::DriveCommand_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Event response(::turtlebot_action_drive::action::DriveCommand_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Event msg_;
};

class Init_DriveCommand_GetResult_Event_request
{
public:
  explicit Init_DriveCommand_GetResult_Event_request(::turtlebot_action_drive::action::DriveCommand_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_DriveCommand_GetResult_Event_response request(::turtlebot_action_drive::action::DriveCommand_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_DriveCommand_GetResult_Event_response(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Event msg_;
};

class Init_DriveCommand_GetResult_Event_info
{
public:
  Init_DriveCommand_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_GetResult_Event_request info(::turtlebot_action_drive::action::DriveCommand_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_DriveCommand_GetResult_Event_request(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_GetResult_Event>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_GetResult_Event_info();
}

}  // namespace turtlebot_action_drive


namespace turtlebot_action_drive
{

namespace action
{

namespace builder
{

class Init_DriveCommand_FeedbackMessage_feedback
{
public:
  explicit Init_DriveCommand_FeedbackMessage_feedback(::turtlebot_action_drive::action::DriveCommand_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::turtlebot_action_drive::action::DriveCommand_FeedbackMessage feedback(::turtlebot_action_drive::action::DriveCommand_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_FeedbackMessage msg_;
};

class Init_DriveCommand_FeedbackMessage_goal_id
{
public:
  Init_DriveCommand_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DriveCommand_FeedbackMessage_feedback goal_id(::turtlebot_action_drive::action::DriveCommand_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_DriveCommand_FeedbackMessage_feedback(msg_);
  }

private:
  ::turtlebot_action_drive::action::DriveCommand_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_action_drive::action::DriveCommand_FeedbackMessage>()
{
  return turtlebot_action_drive::action::builder::Init_DriveCommand_FeedbackMessage_goal_id();
}

}  // namespace turtlebot_action_drive

#endif  // TURTLEBOT_ACTION_DRIVE__ACTION__DETAIL__DRIVE_COMMAND__BUILDER_HPP_
