onkyo-button is a Python script that controls the sound volume on an Onkyo receiver, via a button connected to the GPIO pins on a Raspberry Pi. I've included the instructions here as a record for myself and to share my code with anyone who might want to build a similiar project.

## Requirements
* Raspberry Pi
* Perma-Proto Pi Hat
* [Waterproof Button](http://www.mouser.com/ProductDetail/E-Switch/ULV8F2BSS331/?qs=sGAEpiMZZMvxtGF7dlGNpo%2fFeg65f8WWDggtHu1m1ZQ%3d)
* Michael Elsdörfer's excellent [Onkyo eISCP python library](https://github.com/miracle2k/onkyo-eiscp)
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
* [psutil](https://pypi.python.org/pypi/psutil/)

## Software Install
To install the software just run 
```
pip install onkyo-button
```

# Hardware Construction
Since the button was down an approximately 100' wire, I needed to construct a simple circuit to protect the GPIO pins and the Raspberry Pi.  Here's the circuit design.

![Circuit Design](https://github.com/szaske/onkyo-button/blob/master/images/circuit_design.png)

Here's a picture of the Hat layout:

![PiHat](https://github.com/szaske/onkyo-button/blob/master/images/PiHat.png)

### License
Copyright 2017 Steve Zaske

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

