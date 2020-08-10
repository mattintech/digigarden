# DIGIGarden
DigitGarden is a take on how to make gardening feel like work and not a hobby! (joking!) 

What DIGIGarden is:
DigiGraden is an electronics hobby project that combines gardening, electronics & dev ops for a fun weekend.

What DIGIGarden is not:
This project will not make you a better gardener.

## Getting Started

This project has a few key components:
* Gardening - This is all up to you, what plants to select, when/how to water them.  If the soil has the right pH etc. 
* Ardunio - Will be used to collect sensor data 
* RaspberryPi - This will query the Arduino via RS232 and run the gardenServer API.  The arduino connects to a WiFi access point for the reporting component to collect & store data. In the future I may look at something more power efficent to transmit data, but I had a spare raspberryPi and was easier than trying to make the Ardunio remotely accessible. 
* Reporting - A python script will collect data from the gardenServer API and log it into a postgres DB.  Grafana is used to create a pretty view in to the statistics that are collected over time. 

### Folder Structure
```
DIGIGARDEN
    |
    |__ docker - this contains the docker-compose.yml to build each component
    |
    |__ outdoor - this contains the code for the outdoor devices.
    |
    |__ indoor - this contains the code that is used to query the gardenServer API & 
```

## Support
If you've found an error in this project, please file an issue:
https://github.com/mattintech/digigarden/issues

Patches are encouraged, and may be submitted by forking this project and submitting a pull request through GitHub.

## License
Licensed under the MIT license. See the LICENSE file for details.

## How to make contributions?
Please read and follow the steps in the CONTRIB file.