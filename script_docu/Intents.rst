
*******
Intents
*******
          
This is an autogenerated documentation file for the script: Intents

Run it
------

.. code-block:: sh

	$ ./androanalyze scripts_builtin/Intents.py --package-names com.spotify.music



View the results
----------------

Non-Binary
``````````

.. code-block:: python

	$ ./androquery result -sn Intents -pn com.spotify.music

    	 {
	     "apk meta": {
	         "package name": "com.spotify.music", 
	         "version name": "2.2.0.636", 
	         "sha256": "bbf2c7d7b8fbbce68a97a2f0fd7e854e29b1ea9e3836615e7e6a35095915a607", 
	         "import date": "2015-04-14T15:10:06.364000", 
	         "build_date": "2015-02-11T12:25:40", 
	         "path": "/mnt/stuff/btsync/apks_manual_downloads/02.03.2015_top_free_4/apps_topselling_free/MUSIC_AND_AUDIO/com.spotify.music.apk", 
	         "tag": null
	     }, 
	     "script meta": {
	         "name": "Intents", 
	         "sha256": "db68305576534261d6bde5ce8d13f15a695a074e539c2a6cd42160bab598bbe4", 
	         "analysis date": "2015-06-22T20:29:33.878000", 
	         "version": "0.1"
	     }, 
	     "intents": {
	         "services": {
	             "com_spotify_mobile_android_androidauto_SpotifyMediaBrowserService": {
	                 "action": [
	                     "android.media.browse.MediaBrowserService"
	                 ]
	             }, 
	             "com_spotify_mobile_android_service_RemoteNativeRouterProxy": {
	                 "action": [
	                     "com.spotify.mobile.service.action.COSMOS_PROXY"
	                 ]
	             }
	         }, 
	         "activities": {
	             "com_spotify_mobile_android_ui_activity_TosTextActivity": {
	                 "action": [
	                     "android.intent.action.VIEW"
	                 ], 
	                 "category": [
	                     "android.intent.category.DEFAULT", 
	                     "android.intent.category.BROWSABLE"
	                 ]
	             }, 
	             "com_sony_snei_np_android_account_oauth_BrowserRedirectReceiverActivity": {
	                 "action": [
	                     "android.intent.action.VIEW"
	                 ], 
	                 "category": [
	                     "android.intent.category.DEFAULT", 
	                     "android.intent.category.BROWSABLE"
	                 ]
	             }, 
	             "com_spotify_music_MainActivity": {
	                 "action": [
	                     "android.intent.action.MAIN", 
	                     "android.intent.action.MUSIC_PLAYER", 
	                     "android.nfc.action.NDEF_DISCOVERED", 
	                     "android.intent.action.SEARCH", 
	                     "android.intent.action.VIEW", 
	                     "com.facebook.application.174829003346", 
	                     "android.media.action.MEDIA_PLAY_FROM_SEARCH", 
	                     "com.sonymobile.media.dashboard.ACTION_VIEW_MUSIC_TILE"
	                 ], 
	                 "category": [
	                     "android.intent.category.LAUNCHER", 
	                     "android.intent.category.DEFAULT", 
	                     "android.intent.category.APP_MUSIC", 
	                     "android.intent.category.BROWSABLE"
	                 ]
	             }, 
	             "com_spotify_mobile_android_service_LoginActivity": {
	                 "action": [
	                     "com.spotify.mobile.android.service.action.session.LOGIN"
	                 ], 
	                 "category": [
	                     "android.intent.category.DEFAULT"
	                 ]
	             }, 
	             "com_spotify_mobile_android_arsenal_ArsenalSSOBrowserActivity": {
	                 "action": [
	                     "com.spotify.music.NPAM_ACTION_BROWSER"
	                 ], 
	                 "category": [
	                     "android.intent.category.DEFAULT", 
	                     "android.intent.category.LAUNCHER"
	                 ]
	             }
	         }, 
	         "content providers": {}, 
	         "broadcast receivers": {
	             "com_mixpanel_android_mpmetrics_InstallReferrerReceiver": {
	                 "action": [
	                     "com.android.vending.INSTALL_REFERRER"
	                 ]
	             }, 
	             "com_spotify_music_spotlets_optintrial_TrialAlarmBroadcastReceiver": {
	                 "action": [
	                     "com.spotify.music.spotlets.optintrial.action.TRIAL_REMINDER"
	                 ], 
	                 "category": [
	                     "android.intent.category.DEFAULT"
	                 ]
	             }, 
	             "com_spotify_mobile_android_spotlets_collection_receiver_ConnectionStateChangedReceiver": {
	                 "action": [
	                     "com.spotify.mobile.android.service.broadcast.session.CONNECTION_STATE_CHANGED"
	                 ]
	             }, 
	             "com_spotify_music_spotlets_widget_SpotifyWidget": {
	                 "action": [
	                     "android.appwidget.action.APPWIDGET_UPDATE", 
	                     "com.spotify.mobile.android.ui.widget.PREVIOUS", 
	                     "com.spotify.mobile.android.ui.widget.PLAY", 
	                     "com.spotify.mobile.android.ui.widget.NEXT"
	                 ]
	             }, 
	             "com_spotify_music_internal_receiver_LoggerReceiver": {
	                 "action": [
	                     "com.spotify.music.internal.receiver.CACHE_LOG"
	                 ], 
	                 "category": [
	                     "android.intent.category.DEFAULT"
	                 ]
	             }, 
	             "com_spotify_music_internal_receiver_MediaButtonReceiver": {
	                 "action": [
	                     "android.intent.action.MEDIA_BUTTON"
	                 ]
	             }, 
	             "com_spotify_mobile_android_applink_AppLinkBluetoothManager": {
	                 "action": [
	                     "android.bluetooth.adapter.action.STATE_CHANGED", 
	                     "android.bluetooth.device.action.ACL_CONNECTED", 
	                     "android.bluetooth.device.action.ACL_DISCONNECTED"
	                 ]
	             }, 
	             "com_spotify_music_spotlets_gcm_GcmBroadcastReceiver": {
	                 "action": [
	                     "com.google.android.c2dm.intent.RECEIVE"
	                 ], 
	                 "category": [
	                     "com.spotify.music"
	                 ]
	             }, 
	             "com_spotify_music_spotlets_mobileapptracker_MobileAppTrackerReceiver": {
	                 "action": [
	                     "com.android.vending.INSTALL_REFERRER"
	                 ]
	             }
	         }
	     }
	 }
	 


Binary
``````

For the case that the result may exceed 16MB, it is stored in MongoDB's gridFS. Therefore we need to use a different query syntax:

View the meta data:

.. code-block:: python

	$ ./androquery result -sn Intents -pn com.spotify.music -nd

    	 Empty


View the raw data:

.. code-block:: python

	$ ./androquery result -sn Intents -pn com.spotify.music -nd -r

    	 Empty


Source
------

.. literalinclude:: ../androlyze/scripts_builtin/manifest/components/Intents.py


