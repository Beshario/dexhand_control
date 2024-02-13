from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch

planning_scene_monitor_parameters = { "publish_planning_scene": True, "publish_geometry_updates": True, "publish_state_updates": True, "publish_transforms_updates": True, "publish_robot_description":True, "publish_robot_description_semantic":True}
def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("dexhand", package_name="dexhand_control").to_moveit_configs()
    return generate_demo_launch(moveit_config)
