
## Controlling GPIO and PWM in C/C++ with WiringPi library on Raspberry Pi ##

Check the pins of the RPi 3:

```
$ gpio readall
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
```

### Controlling a led in C/C++ with Wiring Pi ###

Use the next connection for wiring:

![image](/posts/technical/2017-05_controlling_gpio_and_pwm_in_c_cpp_with_wiringpi_library_on_raspberry_pi/rpi3_led.jpg)

Create the file ```test_led.c``` or ```test_led.cpp```:

```
#include <<x>wiringPi.h<x>>
     
#include <<x>stdio.h<x>>
#include <<x>stdlib.h<x>>
#include <<x>stdint.h<x>>
     
int main(void)
{
      
  printf("Raspberry Pi wiringPi led test program\n");
     
  if (wiringPiSetup() == -1)
    exit(1) ;
     
  pinMode(0, OUTPUT);
  int i = 0;
  for(i = 0;i<<x>10;i++){
    digitalWrite(0, HIGH);
    delay(500);
    digitalWrite(0, LOW);
    delay(500);
  }
     
  return 0;
}
```

Compile ```test_led.c``` using:

```
$ gcc -Wall -o test_led test_led.c -lwiringPi
```

Or compile ```test_led.cpp``` using:

```
$ gcc -Wall -o test_led test_led.cpp -lwiringPi
```

Execute using:

```
$ sudo ./test_led
```

So, the led will start blinking for 10 seconds.

### Controlling PWM in C/C++ with Wiring Pi ###

Use the next connection for wiring:

![image](/posts/technical/2017-05_controlling_gpio_and_pwm_in_c_cpp_with_wiringpi_library_on_raspberry_pi/rpi3_pwm.jpg)

Create the file ```test_pwm.c``` or ```test_pwm.cpp```:

```
#include <<x>wiringPi.h<x>>
     
#include <<x>stdio.h<x>>
#include <<x>stdlib.h<x>>
#include <<x>stdint.h<x>>
     
int main(void)
{
     
  printf("Raspberry Pi wiringPi PWM test program\n");
     
  if (wiringPiSetup() == -1)
    exit(1) ;
     
  pinMode(1, PWM_OUTPUT);
  pwmSetRange(10);
  pwmWrite(1, 9) ;  //pwmWrite(PIN, VALUE)
  for(;;){
    delay(1);
  }
     
  return 0;
}
```

Compile ```test_pwm.c``` using:

```
$ gcc -Wall -o test_pwm test_pwm.c -lwiringPi
```

Or compile ```test_pwm.cpp``` using:

```
$ gcc -Wall -o test_pwm test_pwm.cpp -lwiringPi
```

Execute using:

```
$ sudo ./test_pwm
```

So, the intensity of the led will change according the VALUE you choose.


