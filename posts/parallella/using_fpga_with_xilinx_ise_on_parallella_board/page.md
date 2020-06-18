
## Using FPGA with Xilinx ISE on Parallella Board ##

Note: All next steps should be done on PC, not on Parallella Board.

The new Xilinx ISE Design Suite 14 – WebPACK now supports embedded processing design for the Zynq™-7000 All Programmable SoC family for the three smallest Zynq devices – the Z-7010, Z-7020, and Z-7030.

Be careful: that if you use this simple way to program the FPGA: You can't be able to use ARM cores with Linaro/Ubuntu because you modify the parallella.bit.bin (this file contain configuration of Zynq) , then you won't enter with SSH. To use ARM cores with Linaro/Ubuntu and FPGA you should use Vivado and modify part of the entire design (Vivado needs a permanent license, Xilinx gives you a 30-day license).

#### STEP 1: Create project with Xilinx ISE and make .bit bitstream ####

a. Open Xilinx ISE, create project, then make .bit bitstream.

b. When create the project, set the next values:

![image](/posts/parallella/using_fpga_with_xilinx_ise_on_parallella_board/ProjectSettingsFPGA.png)

c. In the .ucf file add the next ```IOSTANDARD=LVCMOS25``` to each physical constraint:

```
... LOC = U19 | IOSTANDARD=LVCMOS25; 
```

d. The connector used on the Parallella Board is the "Expansion Connector GPIO":

![image](/posts/parallella/using_fpga_with_xilinx_ise_on_parallella_board/gpio1.png)

, the corresponding pins on the shield GPIO are:

![image](/posts/parallella/using_fpga_with_xilinx_ise_on_parallella_board/gpio2.png)

, and the correct numeration are:

![image](/posts/parallella/using_fpga_with_xilinx_ise_on_parallella_board/gpio3.png)

e. You can find the pins in pages 28 and 31 of the [https://dennishnf.bitbucket.io/documentation/parallella_board/files/02_parallella_reference_manual.pdf](Parallella Reference Manual)!:  GPIO0_P, GPIO0_N,  GPIO1_P, GPIO1_N, ..., GPIO23_P, GPIO23_N.

#### STEP 2: Convert the bitstream from *.bit to *.bit.bin ####

Note: You should have Vivado installed on your PC to convert from .bit to .bit.bin .

Use this folder bit2bitbin [[https://dennishnf.bitbucket.io/posts/parallella/using_fpga_with_xilinx_ise_on_parallella_board/bit2bitbin.zip](link)!] to convert from .bit to .bit.bin .

a. Copy the bitstream of your project into the folder bit2bitbin.

b. Modify the file called ‘bit2bin.bif’ with the following content (change example.bit with the bitstream of your project):

```
 the_ROM_image:
{
[bootloader]dummy.elf
example.bit
}
```

c. Make sure you have a dummy.elf in that directory.

d. In terminal go to the directory of bit2bitbin folder with ```cd```.

e. Then, run some “magical steps” using the Xilinx tools to convert the bit stream to a loadable bit stream.

```
$ source /opt/Xilinx/Vivado/2015.4/settings64.sh
$ bootgen -image bit2bin.bif -split bin
```

#### STEP 3: Copy the new *.bit.bin file to the boot partion of a Parallella SD card ####

NOTE: before to copy and change the name to parallella.bit.bin, do a backup of your default parallella.bit.bin, this have your configuration of Zynq to set ARM cores with Linaro/Ubuntu.

First you should copy the .bit.bin to the SD card, then change the name to "parallella.bit.bin".

Note: Sync and properly eject the sd card as appropriate for your system.

#### STEP 4: Boot the system ####

Insert the SD card into the Parallella board and boot the system, then run some tests.

After run and finish your project, recover your parallella.bit.bin in the SD card to execute your Linaro/Ubuntu normally.

### Resources ###

-[https://parallella.org/forums/viewtopic.php?f=23&t=134](https://parallella.org/forums/viewtopic.php?f=23&t=134)!.

-[https://www.parallella.org/2015/03/23/new-parallella-elink-fpga-design-project-now-available-in-vivado/](https://www.parallella.org/2015/03/23/new-parallella-elink-fpga-design-project-now-available-in-vivado/)!.

-[https://parallella.org/forums/viewtopic.php?f=51&t=1767](https://parallella.org/forums/viewtopic.php?f=51&t=1767)!.

-[https://parallella.org/forums/viewtopic.php?f=10&t=415](https://parallella.org/forums/viewtopic.php?f=10&t=415)!.


