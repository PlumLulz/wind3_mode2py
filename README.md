# wind3_mode2py
(mode=2) algorithm of zcfgBeWlanGenDefaultKey from libzcfg_be.so in the VMG8828 firmware.

This is the (mode=2) algorithm of zcfgBeWlanGenDefaultKey from libzcfg_be.so in the VMG8828 firmware.\
It's a variant of Zykgen, but does not quite fit within the standard algorithm with just a new charset\
much thanks to Selenium on the hashkiller forum for getting the library cross-compiled and running inside QEMU.\

Usage: python3 wind3_mode2.py S123Y00000001 -pwd_len 16

Credit to drsnooker for his Matlab script that this was converted from: https://forum.hashkiller.io/index.php?threads/unpublished-wpa-key-algorithms.19944/post-342096
