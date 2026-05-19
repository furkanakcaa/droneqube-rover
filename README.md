# DRONEQUBE Indoor Rover — ROS2 + Nav2 Simülasyonu

Bu proje, DRONEQUBE aday görevi kapsamında geliştirilen Indoor AMR (Autonomous Mobile Robot) simülasyonunu içermektedir.

## Görev Tanımı

Gazebo ortamında Nav2 kullanarak bir robotun:

- **Home** konumundan başlayıp
- **A → B → C** noktalarını sırayla ziyaret edip
- Her noktada 1 saniye bekleyip
- Tekrar **Home**'a dönmesini sağlamak

## Kullanılan Teknolojiler

- ROS2 Humble
- Nav2 (Navigation2)
- Gazebo Classic
- Turtlebot3 (Burger)
- Ubuntu 22.04

## Kurulum ve Çalıştırma

```bash
# Bağımlılıkları yükle
sudo apt install ros-humble-turtlebot3* ros-humble-nav2-bringup

# TURTLEBOT3_MODEL ayarla
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc

# Paketi derle
cd ~/waypoint_ws
colcon build --packages-select waypoint_mission
source install/setup.bash
```

### Simülasyonu Başlat

**Terminal 1 — Gazebo:**

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

**Terminal 2 — Nav2:**

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/map.yaml
```

**Terminal 3 — Görev:**

```bash
ros2 run waypoint_mission mission_node
```

## Simülasyon Videosu

[Google Drive — Demo Video](https://drive.google.com/file/d/1shylm-bMfZU8W5Uv048oOHyOBplApGYm/view?usp=drive_link)
