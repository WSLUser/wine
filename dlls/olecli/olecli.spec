name	olecli
type	win16
owner	olecli32

#1 WEP
2 stub OLEDELETE
3 stub OLESAVETOSTREAM
4 stub OLELOADFROMSTREAM
6 stub OLECLONE
7 stub OLECOPYFROMLINK
8 stub OLEEQUAL
9 pascal16 OleQueryLinkFromClip(str word word) OleQueryLinkFromClip16
10 pascal16 OleQueryCreateFromClip(str word word) OleQueryCreateFromClip16
11 pascal16 OleCreateLinkFromClip (str segptr long str segptr word word) OleCreateLinkFromClip16
12 pascal16 OleCreateFromClip(str segptr long str long word word) OleCreateFromClip16
13 stub OLECOPYTOCLIPBOARD
14 pascal16 OleQueryType(ptr segptr) OleQueryType16
15 stub OLESETHOSTNAMES
16 stub OLESETTARGETDEVICE
17 stub OLESETBOUNDS
18 stub OLEQUERYBOUNDS
19 stub OLEDRAW
20 stub OLEQUERYOPEN
21 stub OLEACTIVATE
22 stub OLEUPDATE
23 stub OLERECONNECT
24 stub OLEGETLINKUPDATEOPTIONS
25 stub OLESETLINKUPDATEOPTIONS
26 stub OLEENUMFORMATS
27 stub OLECLOSE
28 stub OLEGETDATA
29 stub OLESETDATA
30 stub OLEQUERYPROTOCOL
31 stub OLEQUERYOUTOFDATE
32 stub OLEOBJECTCONVERT
33 stub OLECREATEFROMTEMPLATE
34 stub OLECREATE
35 stub OLEQUERYRELEASESTATUS
36 stub OLEQUERYRELEASEERROR
37 stub OLEQUERYRELEASEMETHOD
38 stub OLECREATEFROMFILE
39 stub OLECREATELINKFROMFILE
40 stub OLERELEASE
41  pascal OleRegisterClientDoc(ptr ptr long ptr) OleRegisterClientDoc16
42  pascal OleRevokeClientDoc(long) OleRevokeClientDoc16
43  pascal OleRenameClientDoc(long ptr) OleRenameClientDoc16
44 pascal16 OleRevertClientDoc(long) OleRevertClientDoc16
45  pascal OleSavedClientDoc(long) OleSavedClientDoc16
46 stub OLERENAME
47 pascal16 OleEnumObjects(long segptr) OleEnumObjects16
48 stub OLEQUERYNAME
49 stub OLESETCOLORSCHEME
50 stub OLEREQUESTDATA
54 stub OLELOCKSERVER
55 stub OLEUNLOCKSERVER
56 stub OLEQUERYSIZE
57 stub OLEEXECUTE
58 stub OLECREATEINVISIBLE
59 stub OLEQUERYCLIENTVERSION
60 pascal16 OleIsDcMeta(word) OleIsDcMeta16
100 stub DOCWNDPROC
101 stub SRVRWNDPROC
102 stub MFCALLBACKFUNC
110 stub DEFLOADFROMSTREAM
111 stub DEFCREATEFROMCLIP
112 stub DEFCREATELINKFROMCLIP
113 stub DEFCREATEFROMTEMPLATE
114 stub DEFCREATE
115 stub DEFCREATEFROMFILE
116 stub DEFCREATELINKFROMFILE
117 stub DEFCREATEINVISIBLE
200 stub LERELEASE
201 stub LESHOW
202 stub LEGETDATA
203 stub LESETDATA
204 stub LESETHOSTNAMES
205 stub LESETTARGETDEVICE
206 stub LESETBOUNDS
207 stub LESAVETOSTREAM
208 stub LECLONE
209 stub LECOPYFROMLINK
210 stub LEEQUAL
211 stub LECOPY
212 stub LEQUERYTYPE
213 stub LEQUERYBOUNDS
214 stub LEDRAW
215 stub LEQUERYOPEN
216 stub LEACTIVATE
218 stub LEUPDATE
219 stub LERECONNECT
220 stub LEENUMFORMAT
221 stub LEQUERYPROTOCOL
222 stub LEQUERYOUTOFDATE
223 stub LEOBJECTCONVERT
224 stub LECHANGEDATA
225 stub LECLOSE
226 stub LEGETUPDATEOPTIONS
227 stub LESETUPDATEOPTIONS
228 stub LEEXECUTE
229 stub LEOBJECTLONG
230 stub LECREATEINVISIBLE
300 stub MFRELEASE
301 stub MFGETDATA
302 stub MFSAVETOSTREAM
303 stub MFCLONE
304 stub MFEQUAL
305 stub MFCOPY
307 stub MFQUERYBOUNDS
308 stub MFDRAW
309 stub MFENUMFORMAT
310 stub MFCHANGEDATA
400 stub BMRELEASE
401 stub BMGETDATA
402 stub BMSAVETOSTREAM
403 stub BMCLONE
404 stub BMEQUAL
405 stub BMCOPY
407 stub BMQUERYBOUNDS
408 stub BMDRAW
409 stub BMENUMFORMAT
410 stub BMCHANGEDATA
500 stub DIBRELEASE
501 stub DIBGETDATA
502 stub DIBSAVETOSTREAM
503 stub DIBCLONE
504 stub DIBEQUAL
505 stub DIBCOPY
507 stub DIBQUERYBOUNDS
508 stub DIBDRAW
509 stub DIBENUMFORMAT
510 stub DIBCHANGEDATA
600 stub GENRELEASE
601 stub GENGETDATA
602 stub GENSETDATA
603 stub GENSAVETOSTREAM
604 stub GENCLONE
605 stub GENEQUAL
606 stub GENCOPY
608 stub GENQUERYBOUNDS
609 stub GENDRAW
610 stub GENENUMFORMAT
611 stub GENCHANGEDATA
701 stub ERRSHOW
702 stub ERRSETDATA
703 stub ERRSETHOSTNAMES
704 stub ERRSETTARGETDEVICE
705 stub ERRSETBOUNDS
706 stub ERRCOPYFROMLINK
707 stub ERRQUERYOPEN
708 stub ERRACTIVATE
709 stub ERRCLOSE
710 stub ERRUPDATE
711 stub ERRRECONNECT
712 stub ERRQUERYPROTOCOL
713 stub ERRQUERYOUTOFDATE
714 stub ERROBJECTCONVERT
715 stub ERRGETUPDATEOPTIONS
716 stub ERRSETUPDATEOPTIONS
717 stub ERREXECUTE
718 stub ERROBJECTLONG
800 stub PBLOADFROMSTREAM
801 stub PBCREATEFROMCLIP
802 stub PBCREATELINKFROMCLIP
803 stub PBCREATEFROMTEMPLATE
804 stub PBCREATE
805 stub PBDRAW
806 stub PBQUERYBOUNDS
807 stub PBCOPYTOCLIPBOARD
808 stub PBCREATEFROMFILE
809 stub PBCREATELINKFROMFILE
810 stub PBENUMFORMATS
811 stub PBGETDATA
812 stub PBCREATEINVISIBLE
910 stub OBJQUERYNAME
911 stub OBJRENAME
912 stub OBJQUERYTYPE
913 stub OBJQUERYSIZE
950 stub CONNECTDLGPROC
951 stub SETNETNAME
952 stub CHECKNETDRIVE
953 stub SETNEXTNETDRIVE
954 stub GETTASKVISIBLEWINDOW
