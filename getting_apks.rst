************
Getting APKs
************

`AndroLyze` has an easy way to download APKs from the `PlayStore` through `GooglePlayCrawler <https://github.com/Akdeniz/google-play-crawler>`_.



Requirements
------------

The docker image has not initialized this git submodule by default. So we need to do this first:

.. code-block:: sh

    $ worker@f6a8d4e49d39:/home/worker/androlyze$ git submodule update --init google-play-crawler
    $ worker@f6a8d4e49d39:/home/worker/androlyze$ ln -s google-play-crawler/googleplay/googleplaycrawler-0.3.jar googleplaycrawler.jar
    $ worker@f6a8d4e49d39:/home/worker/androlyze$ cp google-play-crawler/googleplay/crawler.conf conf/crawler.conf


Be sure you have done the following steps before using the google play crawler:

* Set email and password in conf/crawler.conf
* Get androidid via "java -jar googleplaycrawler.jar -f conf/crawler.conf checkin" and set in in the config file


Download
--------

Check that the crawler is working by listing all categories in Google Play


.. code-block:: sh

    worker@f6a8d4e49d39:/home/worker/androlyze$ ./playstore.py list
    GAME
    BOOKS_AND_REFERENCE
    BUSINESS
    COMICS
    COMMUNICATION
    EDUCATION
    ENTERTAINMENT
    FINANCE
    HEALTH_AND_FITNESS
    LIBRARIES_AND_DEMO
    LIFESTYLE
    APP_WALLPAPER
    MEDIA_AND_VIDEO
    MEDICAL
    MUSIC_AND_AUDIO
    NEWS_AND_MAGAZINES
    PERSONALIZATION
    PHOTOGRAPHY
    PRODUCTIVITY
    SHOPPING
    SOCIAL
    SPORTS
    TOOLS
    TRANSPORTATION
    TRAVEL_AND_LOCAL
    WEATHER
    APP_WIDGETS


Download an APK by name:

.. code-block:: sh

    worker@f6a8d4e49d39:/home/worker/androlyze$ ./playstore.py download_pn com.facebook.katana

Download the top free 500 applications from every category:

.. code-block:: sh


    worker@f6a8d4e49d39:/home/worker/androlyze$ ./playstore.py download_top_all_categories 500
    Downloading the apps_topselling_free apks from category: GAME
    Downloading: com.gamehivecorp.taptitans, com.vg.citybussimulator2015, com.uu.generaladaptiveapps, br.com.tapps.cowevolution, com.king.alphabettysaga, air.com.puffballsunited.escapingtheprison, com.studio7775.BeatMP3v2, com.miniclip.eightballpool, com.rovio.angrybirdsfight, com.tabtale.crazypoolparty, com.ea.game.simpsons4_row, com.Seriously.BestFiends, com.supercell.hayday, com.rovio.angrybirds, com.bigkraken.thelastwar, com.ea.games.simsfreeplay_row, com.prettysimple.criminalcaseandroid, com.aim.racing, com.boombit.Spider, com.rr.generaladaptiveapps, com.scimob.ninetyfour.percent, se.feomedia.quizkampen.de.lite, com.pinkpointer.wordsearch, com.SimgeSimulation.Woodball, com.king.farmheroessaga, com.nenoff.followthelinefree, com.halfbrick.fruitninjafree, com.ea.game.tetris2011_row, com.supercell.boombeach, com.midasplayer.apps.bubblewitchsaga2, com.glu.t5, com.ea.game.pvzfree_row, com.ping9games.grabtheauto3, com.sometimeswefly.littlealchemy, com.ammonite.dotmuncher, com.halfbrick.jetpackjoyride, com.aa.generaladaptiveapps, com.machinezone.gow, com.bigfishgames.gummydropgoogle, com.fgol.HungrySharkEvolution, com.snailgameusa.tp, com.ff.generaladaptiveapps, com.explorationbase.ExplorationLite, com.mangoogames.emojiquiz, com.ea.games.r3_row, multicraft.worldcraft.world, com.hugogames.superskater, com.Artibus.CircleMaster, com.netmarble.mherosgb, com.robtopx.geometryjumplite, com.squareenix.relicrun, com.mobirix.slideking, com.ea.game.fifa15_row, com.uken.BingoPop, com.roostergames.hillclimbtruckracing3, com.blizzard.wtcg.hearthstone, com.outfit7.mytalkingtomfree, com.ssc.fitfat, org.orangenose.games, com.yangyu.realskate, com.zynga.farmarcade, com.zynga.FarmVille2CountryEscape, com.natenai.glowhockey, com.lego.ninjago.toe, com.fingersoft.hillclimb, com.platogo.pmp, com.imangi.templerun2, com.lima.doodlejump, com.nordcurrent.canteenhd, com.wagawin.android2, com.hugogames.hugotrollrace, com.hcg.cok.gp, block.city.game, com.gameloft.android.ANMP.GloftDMHM, com.iwin.dond, com.doubleugames.DoubleUCasino, fr.x_studios.x_laser_2, com.kiloo.subwaysurf, software.simplicial.nebulous, com.ovilex.bussimulator2015, com.yodo1.crossyroad, com.game.wer.wird.millionaer, com.mangolee.amazon.free.card.cuteslots, com.king.candycrushsodasaga, de.lotum.whatsinthefoto.de, com.degoo.android.pregnantdoctor, com.BitofGame.MiniGolfRetro, com.supercell.clashofclans, com.tp.android.plasticsurgery, com.hammerhead.furious7, com.notdoppler.earntodie2, com.miniclip.dudeperfect, jp.gree.warofnationsbeta, me.pou.app, com.outfit7.mytalkingangelafree, com.fireflygames.rushofheroes, com.king.candycrushsaga, com.igg.castleclash_de, br.com.tapps.giraffeevolution, com.umbrella.boomdots
    Downloading...com.gamehivecorp.taptitans : 61881468 bytes


Update Database
---------------

Update all APKs with a newer version available in the `PlayStore` :

.. code-block:: sh

    worker@f6a8d4e49d39:/home/worker/androlyze$ ./androquery -idb dbs/test.idb import package-names | ./androupdate.py dbs/test.idb

The first command lists all package names from the import database. The seconds reads them from `stdin` and checks each for a newer version. If this is the case, it gets downloaded.

Manual
------

.. code-block:: sh

    worker@f6a8d4e49d39:/home/worker/androlyze$ ./playstore.py
    Usage: ./playstore.py <list
                           |download_new_all_categories <number>
                           |download_top_all_categories <number>
                           |download <category> <subcategory> <number>
                           |download_pn <package_name>
                          >

    The script relies on google-play-crawler.

    Be sure you have done the following steps before using this script!
    1) Get it from here: https://github.com/Akdeniz/google-play-crawler
    and place this script inside the googleplay directory after it has been build.
    2) Set email and password in crawler.conf
    3) Get androidid via "java -jar googleplaycrawler.jar -f crawler.conf checkin" and set in in the config file
    4) playstore.py benutzen ;)

    Example: ./playstore.py download WEATHER apps_topselling_new_free 2
    Example: ./playstore.py download_pn a2dp.Vol
    Example: ./playstore.py list
    Example: ./playstore.py download_new_all_categories 10
    Example: ./playstore.py download_top_all_categories 10

    Possible subcategories are:
        apps_topselling_paid
        apps_topselling_free
        apps_topgrossing
        apps_topselling_new_paid
        apps_topselling_new_free
