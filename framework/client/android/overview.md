# Android
## Overview
2003年10月，Andy Rubin等人创建Android公司，并组建Android团队。
2005年8月: 由Google收购注资，Andy Rubin开发
2007年11月: Google牵头硬件制造商组建开放手机联盟共同研发改良Android系统
2008年10月: 第一步手机G1发布
2009年9月: 推出了搭载Android 1.6正式版的手机HTC Hero(G3)
2011年8月: Android手机已占据全球智能机市场48%的份额
2013年11月: Android4.4 KitKat(奇巧巧克力)
2014年10月: Android 5.0 Lollipop(棒棒糖)
2015年9月: Android 6.0 Marshmallow（棉花糖）
2016年8月: Android 7.0 Nougat（牛轧糖）
2017年8月: Android 8.0O Reo（奥利奥）
2018年5月: Android 9.0 Pie (派)

Android 是运行于Linux kernel之上，但并不是GNU/Linux. Android又以Bionic 取代Glibc、以Skia 取代Cairo、再以opencore取代FFmpeg等等。Android 为了达到商业应用，必须移除被GNU GPL授权证所约束的部份，例如Android将驱动程序移到 Userspace，使得Linux driver 与 Linux kernel彻底分开。Bionic/Libc/Kernel/ 并非标准的Kernel header files。Android 的 Kernel header是利用工具由 Linux Kernel header 所产生的，这样做是为了保留常数、数据结构与宏。

如果你将apk文件传到/system/app文件夹下会发现执行是不受限制的。
Android 的HAL（硬件抽像层）