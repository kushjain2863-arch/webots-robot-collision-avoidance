# Webots Collision Avoidance Demo

This project contains a simple Webots simulation where:
- a custom 2-wheel differential-drive robot moves around the arena,
- an e-puck robot moves independently,
- the custom robot uses distance sensors to detect the e-puck and avoid it.

The project includes:
- a custom controller for the 2-wheel robot,
- a controller for the moving e-puck,
- a Webots world file that loads both robots,
- step-by-step instructions from installation to running the simulation.

## Repository structure

- `controllers/robot_avoider/robot_avoider.py` — main avoidance logic
- `controllers/e_puck_mover/e_puck_mover.py` — moving e-puck logic
- `worlds/robot_avoidance.wbt` — Webots simulation world
- `README.md` — setup and usage instructions

## What the simulation does

The custom robot is a simple differential-drive vehicle with:
- two wheel motors,
- four distance sensors,
- a simple obstacle-avoidance rule.

The e-puck robot patrols the environment in a looping motion. When the custom robot gets close to the moving e-puck, the sensor readings rise, and the custom robot reverses and turns away to avoid a collision.

## Quick start

1. Install Webots from the official Webots website.
2. Open this folder as a Webots project.
3. Open `worlds/robot_avoidance.wbt`.
4. Click the Run button in Webots.
5. Watch the custom robot avoid the moving e-puck.

## Tuning

You can modify these values in `robot_avoider.py`:
- `OBSTACLE_THRESHOLD` — the distance value used to decide if an obstacle is too close
- `FORWARD_SPEED` — speed while moving forward
- `TURN_SPEED` — speed while turning away from an obstacle

This makes it easy to experiment with different avoidance behaviors.
