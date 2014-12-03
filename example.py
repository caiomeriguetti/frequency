#coding=utf-8

from frequency import Frequency

fr=Frequency(3) #execute 3 times by sec

while 1:

	fr.start()

	print 'This is executed 3x by sec'

	fr.end()