# Battery Monitor

ROS 2 node pro sledování stavu baterie a publikaci varování (`LOW`, `OVERHEAT`, `OK`) na základě napětí a teploty.

## Topic:
- Subscribuje: `/readings` (`battery_msg/BatteryStatus`)
- Publikuje: `/battery_alert` (`std_msgs/String`)
