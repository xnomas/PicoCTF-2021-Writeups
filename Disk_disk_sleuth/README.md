# Disk,disk,sleuth!

Category: Forensics </br>
AUTHOR: SYREAL

**Disclaimer! I do not own any of the challenge files!**

## Description
```
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz
```

## The image

After downloading the image, I used `gunzip` to unzip it and then ran `srch_strings` just as recommended. 
</br>

*NOTE: srch_strings is part of the sleuthkit, which you can downloade [here](https://sleuthkit.org/sleuthkit/download.php)*
</br>

```
srch_strings dds1-alpine.flag.img
...
mouse
mousedev.ko
serio
psmouse.ko
@1,`@1,`@1,`
@1,`@1,`@1,`
@1,`@1,`@1,`
@1,`@1,`@1,`
@1,`@1,`@1,`
@1,`@1,`@1,`
@1,`@1,`@1,`
@1,`@1,`@1,`
hyperv-keyboard.ko
pcips2.ko
bcache
dm-bio-prison.koHp
dm-bufio.ko
dm-cache-smq.ko
dm-cache.ko
dm-crypt.ko
dm-delay.ko
dm-flakey.koNp
dm-log-userspace.ko
dm-log-writes.koPp
dm-log.ko
dm-mirror.koRp
dm-mod.ko
dm-multipath.ko
dm-queue-length.ko
dm-raid.ko
dm-region-hash.ko
dm-round-robin.ko
dm-service-time.ko
dm-snapshot.ko
dm-switch.ko[p
dm-thin-pool.ko
dm-unstripe.ko
...
```
But the output is absolutely massive... Hey, maybe we can just do a simple grep?
```
srch_strings dds1-alpine.flag.img | grep pico
ffffffff81399ccf t pirq_pico_get
ffffffff81399cee t pirq_pico_set
ffffffff820adb46 t pico_router_probe
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_267e38f6}
```
Flagalicious! 