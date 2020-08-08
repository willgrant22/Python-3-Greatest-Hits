#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "[¦\x85\x1a\x06\x0c\x8e\x10\x85\x87\x9cU.ÍïIMG0V¬º\x8bãÁ\x81SÙçº\x9bstñ\x97··\xa0´Í¹R#Ø\x10\x8aÀ·ði¸\x97jL*\xad¿\x0cÜDâv\x14ñîÆü4mª4×}Æ\x7f:Rg""\x17[øÀr\x8cv/æ{\x98ÔZiþÞ\x13\x11\x8c\x93l\x0cúijö¿¬úo,å4lq8S\x95\x8e&8\x1d\x0bp;Ë\x12X½\x1b\x81õe®XïP\x81\x8aE\x8a§\x96õaT¸uñ\x15_|]3Î¾O\\æ\r\x16ï\x1d\x03ß¯\x8fÏôÿß\x8f>í(¦cÜvÎ\x8b\x16\x0c£§\n\x05í¡:êÞ>±\x88\x9d8\x98§Ó«6I)ÓûØþuùBø`¯þém\x02ÜÇj¯\x01þ\x07¤èG\x96íwÎ""\x9a\x137Þè]R\x18\xa0\x8cº¦áFÌ<\x85\x8e\x9f9\x1f¸\x05w\x83]
ëù\x94Øå\x8c`øð®G¾Ìb]½-\x00µ:=q«Èv±\x8fK\x06>t^ùYM\x1fü\x8bà\x155\x1d3ê}oãá\x8a\x12\x96¹_SZ\x00ÿ^S6*Ñ\x15ro¶"\x8al¿\x81\x04/D +\r\x98\x07¡<\x0bz\x9fï8=¶*¥1å\x9c>ì\x07\x11\x83ò:¥;\x05r!®ÇÍÑ""u\x83,§\x02Zh\x13\x9a½)I\x03µH\x87\x10æð?ÍªùkæN\x11Â$ïÎ=:ÿácÈ\x1du¾(NÐm|\x8dyÿ\x01}OO\x9c_UÀ¨\x02¡\x04;Ö[øY>HÂ\x93/¢\x1e\x99\x1d-iY²Ý)\x08ÂI<\x8fþ\x1f\t4Ø\x96\x9d\x11»\x82§f\x97ïe\x04-È(,;WTÐ>\x82\x00ÀTÿ:;¨»ÓIÜy¦a\x0c¶Û® ³Ô\x91r«\xa0B\x80\x97t\x9eä[a²y]"
# encrypt
pyAesCrypt.encryptFile("passwords.xlsx", "data.Lock", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.Lock", "dataout.db", password, bufferSize)