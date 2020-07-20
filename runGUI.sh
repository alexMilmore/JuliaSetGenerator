# Allows docker image to be run while still using the display
echo "Running a docker gui file"
sudo docker run -i -t --rm \
-e DISPLAY=$DISPLAY \
--user $(id -u):$(id -g) \
-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
--name="juliaGUI" julia
