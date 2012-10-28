#!/bin/sh
#
# Startup script for the jjproxy
#
# pidfile: ./jjproxy.pid

jjproxy=./jjproxy.py
[ -f $jjproxy ] || exit 0

pidfile=./jjproxy.pid

RETVAL=0

# See how we were called.
case "$1" in
  start)
        echo "Starting jjproxy: "
         $jjproxy --pidfile $pidfile &
        ;;
  stop)
        if [ -f $pidfile ]; then
        processcheck="ps -c"
        if $processcheck `cat $pidfile` > /dev/null; then
            echo "Shutting down jjproxy: "
            kill -9 `cat $pidfile`
            rm $pidfile
        fi
        RETVAL=$?
        [ $RETVAL -eq 0 ] && rm -f $pidfile
        fi
        ;;
  restart)
	$0 stop
	$0 start
	RETVAL=$?
	;;
  *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
esac

exit $RETVAL

