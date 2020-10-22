Nethserver-wordpress is a rpm integration to install wordpress from epel to Nethserver

Once installed You have to point your browser to the url http://url/wordpress and set all informations needed.

You have some db which allows to use specific settings

	wordpress=configuration
	     MaxExecutionTime=60
	     MemoryLimit=128M
	     PostMaxSize=32M
	     UploadMaxSize=8M
	     WebFilesMod=enabled    #used to allow upgrade files&folder with the backend
	     access=public          #You can restrict to your local network or be opened to all (public/private) 
	     status=enabled         #you can disabled completely worpdress (enabled/disabled)

If you want to change something, for example (don't forget M which means megabytes)

	config setprop wordpress UploadMaxSize 10M
	signal-event nethserver-wordpress-update

You have also some hidden db : 

If you want to force all users to renew their authentications each time you do a signal-event (enabled/disabled)

	config setprop wordpress Salt enabled
	signal-event nethserver-wordpress-update

If you want to enable the 'Debug' mode of wordpress (enabled/disabled)

	config setprop wordpress Debug enabled
	signal-event nethserver-wordpress-update

If you want that all themes & plugins can be updated automatically (enabled/disabled)

	config setprop wordpress AutomaticUpdater enabled
	signal-event nethserver-wordpress-update

If you want to use another name instead of 'wordpress' (http://url/wordpress), the older 'wordpress' is not removed

	config setprop wordpress URL foldername
	signal-event nethserver-wordpress-update

If you've placed Wordpress in its own virtual host, and you want to use a separate TLS certificate (_i.e.,_ not the default server certificate) for that virtual host

	config setprop wordpress CrtFile /path/to/certificate
	config setprop wordpress ChainFile /path/to/chain
	config setprop wordpress KeyFile /path/to/key
	signal-event nethserver-wordpress-update

