sudo docker pull osgeo/gdal:ubuntu-small-3.6.3
sudo docker images

sudo docker run -dit --name gdal_container osgeo/gdal:ubuntu-small-3.6.3 bash
sudo docker ps
sudo docker exec -it gdal_container bash # enter the container

#==========================================================================
# run this inside the container
#==========================================================================
mkdir workspace
cd workspace
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install pandas
#==========================================================================


#==========================================================================
# press ctrl+d to exit from container and run this outside of the container
#==========================================================================
sudo docker cp create_shape.py gdal_container:/workspace
sudo docker cp read_shape.py gdal_container:/workspace
# then enter the container again to test running the python script
#==========================================================================

sudo docker login
sudo docker commit gdal_container wawancenggoro/gdal_pandas:latest
sudo docker push wawancenggoro/gdal_pandas:latest

sudo docker rm -f gdal_container
sudo docker rmi -f wawancenggoro/gdal_pandas:latest
sudo docker rmi -f osgeo/gdal:ubuntu-small-3.6.3