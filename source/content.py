"""Editorial data for GTASIX (checked against official sources on 2026-11-18)."""
ROCKSTAR='https://www.rockstargames.com/VI'
PS5='https://www.playstation.com/en-us/games/grand-theft-auto-vi/'
PS5SSD='https://www.playstation.com/en-us/support/hardware/ps5-install-m2-ssd/'
XBOX='https://news.xbox.com/en-us/2020/09/24/xbox-series-x-and-xbox-series-s-custom-storage-solution-primer/'
PRELOAD='https://support.rockstargames.com/articles/7nPqOA2uCbpEQHXx7KVrYd/grand-theft-auto-vi-pre-load-faq'
RELEASE='https://support.rockstargames.com/articles/29jV3Cv2cCgvwM1XgtMO5o/grand-theft-auto-vi-regional-pre-load-and-release-times-on-playstation-5-and-xbox-series-x-or-s'
EDITION='https://support.rockstargames.com/articles/4QfG4FmZCf5W1gS8jy4UVT/grand-theft-auto-vi-platform-editions-and-versions'
PERFORMANCE='https://www.rockstargames.com/newswire/article/89834o94713o21/pre-load-grand-theft-auto-vi-now'
TRAILERS='https://www.rockstargames.com/VI/media/videos'
STORAGE='https://www.playstation.com/en-us/accessories/storage-solutions/'
STORE='https://store.rockstargames.com/game/buy-gta-vi'

categories=[
 ('launch','Launch & editions','The dates, prices, editions, unlock times and day-one checklist.','calendar-days','01'),
 ('storage','Storage & SSD','Install size, expansion drives, how to make enough room.','hard-drive','02'),
 ('troubleshooting','Troubleshooting','Preload, downloads, licenses, installs and connection issues.','wrench','03'),
 ('platforms','Platforms & performance','PS5, PS5 Pro, Xbox Series X|S, PC and graphics.','gamepad-2','04'),
 ('gameplay','Gameplay & tips','Starter tips, controls, progress and spoiler-conscious help.','crosshair','05'),
 ('world','Leonida & story','Characters, locations, the world and story reveals.','map-pin','06'),
 ('collectibles','Completion & secrets','Collectibles, achievements, cheats and verified discoveries.','trophy','07'),
 ('media','Videos & news','Official gameplay, trailers, analysis and trusted sources.','clapperboard','08'),
]

articles=[]
def add(slug,title,cat,summary,answer,steps,faqs,sources=None,status='CONFIRMED',read=4,callout=None,aliases=None):
    articles.append(dict(slug=slug,title=title,category=cat,summary=summary,answer=answer,steps=steps,faqs=faqs,sources=sources or [ROCKSTAR],status=status,read=read,callout=callout,aliases=aliases or []))

add("gta-6-release-date-and-time","GTA 6 Out Now: Release Date, Consoles and PC Status","launch","GTA VI is out now on PS5 and Xbox Series X|S. See Rockstar's launch announcement and which platforms can play.","Rockstar announced GTA VI is available worldwide on November 19, 2026 for PS5 and Xbox Series X|S. A PC release date has not been announced. PS4 and Xbox One are not launch platforms. If your console still shows a lock, confirm its store license and game updates.",["Check you are using PS5, PS5 Pro or Xbox Series X|S, the announced launch consoles.","Open your owned games library with the purchasing or code-redemption account.","Install the full game, game updates and console firmware, leaving free SSD headroom.","If locked, check the store region and game entitlement. Restart the console or restore licenses before reinstalling.","For your first session, use the settings and saving guides linked on this page."],[["Is GTA 6 out yet?","Yes. Rockstar's November 19, 2026 announcement confirms launch on PS5 and Xbox Series X|S."],["Can I play GTA 6 on PC?","Rockstar has not announced a PC launch date as of November 19."],["Is GTA 6 on PS4?","No PS4 or Xbox One launch has been announced."],["Can I play on PS5 Pro?","Yes. PS5 Pro is within the supported PS5 family."]],sources=["https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available","https://www.rockstargames.com/VI/out-now"],status="CONFIRMED",read=5,aliases=["is gta 6 out","gta 6 release date","gta 6 pc availability","gta vi console launch"])

add('gta-6-best-price-where-to-buy','Where to buy GTA 6 cheapest: U.S. PS5 and Xbox deals','launch',
'Compare $79.99 Standard Edition prices at major U.S. retailers, potential rewards and code-in-box pitfalls.',
'As checked November 18, 2026, the GTA VI Standard Edition is $79.99 at PlayStation Store, Xbox Store, Walmart, Target and Best Buy. Discount eligibility, rewards and checkout taxes determine the actual cheapest final price. The current retail case contains a download code, not a disc.',
['Choose your platform first: PS5, PS5 Pro or Xbox Series X|S, and confirm compatibility on the store page.',
 'Check the official digital storefront and major trusted retailers for current price and availability; see the GTASIX Buy / Deals page for links.',
 'Look for legitimate savings already available to you: qualified retailer card discounts, earned rewards or a valuable trade-in.',
 'Compare the final cart total including shipping and tax. A small sticker-price saving can disappear in delivery costs.',
 'Avoid unverified third-party accounts, suspicious cheap key sellers, VPN region switching and early-access scams.'],
[('What is the cheapest official GTA 6 price?','The mainstream U.S. Standard Edition listings checked November 18, 2026 were $79.99 before tax. Store-specific or card discounts may change your final total.'),('Is the GTA 6 physical edition on disc?','No. Rockstar says the physical code-in-box edition contains a download code, not a disc.'),('Does Target Circle Card save 5% on GTA 6?','Target generally advertises a 5% discount for eligible purchases with its Circle Card. GTA software is excluded from some separate promotions. Check actual eligibility in your cart.')],
['https://www.rockstargames.com/VI','https://store.playstation.com/en-us/product/EP1004-PPSA01547_00-GTAVISTANDARD001/','https://www.xbox.com/en-US/games/store/p/9P3H4968GRSM','https://www.target.com/c/target-circle-card-program-rules/-/N-4tgj0','https://www.bestbuy.com/product/grand-theft-auto-vi-code-in-box-playable-11-19-26-playstation-5/6684968'],read=5,aliases=['gta vi cheap','gta 6 best deal','gta vi price comparison','where to preorder gta6'])

add('how-to-preload-gta-6','How to preload GTA 6 on PS5 or Xbox','launch',
'Install GTA VI before launch, including auto-download settings and what to do if it is missing.',
'Digital GTA 6 preloading opened November 10, 2026, on PS5 and Xbox Series X|S for eligible pre-orders. On PS5 it began at midnight local time; on Xbox it began at 00:00 GMT.',
['Open your console store or Game Library and find Grand Theft Auto VI under purchased or pre-ordered titles.',
 'Select Download or Pre-install if available; if your console offers auto-download, enable it.',
 'PS5: Settings → Saved Data and Game/App Settings → Automatic Updates and configure Auto-Download; Rest Mode network access helps.',
 'Xbox: check My games & apps → Full library → Owned games or the queue, and confirm your power/network settings permit downloads.',
 'Leave your console connected, monitor available storage, and verify the full install completes before release.'],
 [('Is GTA 6 preload live?','Yes. Rockstar announced digital preloading was available beginning November 10, 2026.'),('Can I play a preloaded copy early?','No. Preload allows downloading encrypted game files before the normal unlock time.'),('Can I preload a physical copy?','The 2026 physical code-in-box version supplies a download code; redeem the code to preload. There is no game disc in the box.')],[PRELOAD,PERFORMANCE,EDITION],read=5,aliases=['gta6 preorder download','gta 6 pre install','preload game'])

add('gta-6-editions-compared','GTA 6 Standard vs Ultimate Edition: what changes?','launch',
'Compare the actual editions and avoid paying for an upgrade you do not want.',
'Rockstar lists Standard and Ultimate editions. Standard includes the game; Ultimate adds a separate collection of bonus content. A paid Ultimate upgrade can be purchased later.',
['Start with the Standard Edition if you primarily care about the story and base game.',
 'Open the official Rockstar Store or console storefront and compare the Ultimate bonus list for your region.',
 'Decide whether the additional cosmetic, vehicle and gameplay extras are valuable to you; the base game remains playable with Standard.',
 'If unsure, note that Rockstar supports a separate Ultimate Edition Upgrade after purchasing Standard.'],
 [('Is the Ultimate Edition required for GTA 6?','No. Standard contains the base game.'),('Can I upgrade later?','Yes, Rockstar lists a separate Ultimate Edition Upgrade.'),('Does the boxed GTA 6 include a disc?','No. Rockstar says the physical 2026 version contains a digital download code.')],[EDITION,STORE],read=4)

add('gta-6-preorder-bonuses','GTA 6 preorder bonuses explained','launch',
'Find out what the Vintage Vice City Pack includes and what is region or edition dependent.',
'Rockstar advertises a Vintage Vice City Pack for eligible preorders, including a 1955 Vapid Stanier Sedan and Garage, outfits/hairstyles and an exclusive weapon pattern. Eligibility and included offers vary by store.',
['Check the official game store listing for your platform and region before buying.',
 'Compare any currently shown preorder cutoff and item eligibility; make a screenshot or save the receipt.',
 'Ensure the digital code or account matches your console store territory.',
 'If the bonus does not appear after release, consult the retailer entitlement details before reordering.'],
 [('What is the Vintage Vice City Pack?','Rockstar lists a themed car/garage, cosmetics and a weapon pattern for qualifying orders.'),('Is the preorder bonus required to play?','No. These are optional extras.'),('Do all regions get identical rewards?','Check your region’s official store listing, which controls eligibility.')],[EDITION,STORE],read=4)

add('gta-6-launch-day-checklist','The complete GTA 6 launch-day checklist','launch',
'A spoiler-free ten-minute readiness routine before you hit Play.',
'Have a compatible console, the correct game entitlement, enough SSD storage, completed preload, current firmware and a working controller before the November 19 unlock.',
['Verify you own or redeemed GTA VI in the same PlayStation/Xbox account you plan to play on.',
 'Check storage now; PlayStation’s GTA VI page recommends at least 212 GB of free PS5 space.',
 'Finish preload and confirm the queued download is not paused or waiting on an update.',
 'Update console system software; ensure your account can sign in and that your controller is charged.',
 'Avoid unverified “early unlock” tricks, suspicious patch files and third-party login pages.'],
 [('How much free PS5 space is advised?','PlayStation says to clear at least 212 GB before preload.'),('Do I need to buy a second SSD?','Not if you already have sufficient free compatible storage.'),('Will a game patch need additional room?','Possibly. Keeping a little extra free space is prudent.')],[PS5,PRELOAD,STORAGE],read=4)

add('gta-6-download-size-ps5-xbox','GTA 6 download size & required storage on PS5 and Xbox','storage',
'Understand the verified PS5 minimum and why Xbox space may vary.',
'PlayStation’s official GTA VI page recommends clearing a minimum of 212 GB on PS5. Do not assume the exact Xbox install size is identical; check your Xbox download queue or store listing.',
['On PS5 go to Settings → Storage and inspect free Console Storage or installed M.2 SSD space.',
 'Keep at least 212 GB free for the PS5 game; leave extra headroom for patches and downloads.',
 'On Xbox open My games & apps → Manage → Storage devices, then consult your GTA VI install detail for the current size.',
 'Remove or move older games if needed; use the storage checker tool to calculate your gap.'],
 [('How many GB is GTA 6?','PlayStation recommends at least 212 GB free on PS5; actual downloaded and installed sizes can differ.'),('Is 212 GB the confirmed Xbox size?','No. Verify the Xbox size in its game detail/install queue.'),('Can I use a normal USB hard drive to play?','On PS5, PS5 titles must be played from internal or compatible M.2 SSD storage, not USB. Xbox Series X|S optimized games generally need internal or supported expansion-card storage.')],[PS5,PS5SSD,XBOX],read=5,aliases=['gta6 file size','gta vi storage requirements','how many gb gta 6'])

add('free-up-space-on-ps5-for-gta-6','How to free up 212 GB on PS5 for GTA 6','storage',
'What to delete, move or capture-backup before installing GTA VI.',
'Use Settings → Storage to see what is taking room. Delete rarely played games or move eligible games, video captures and other files before downloading GTA 6.',
['Open Settings → Storage → Console Storage to review games/apps and media gallery sizes.',
 'Remove old game installations you can redownload later; do not delete saved-data backups without checking what is preserved.',
 'Move PS5 titles to a compatible M.2 expansion SSD if available; or move them to USB for archival storage only.',
 'Clear unnecessary captures and keep a margin above the official 212 GB recommendation.',
 'Launch the preload again and verify it installs fully.'],
 [('Will deleting an installed game erase my saves?','Game application files and save data are managed separately on PS5, but confirm before deleting anything.'),('Can I move GTA 6 to a USB drive to play?','PS5 games cannot launch from ordinary USB extended storage.'),('How much extra space should I keep?','212 GB is PlayStation’s stated minimum; additional headroom for patches is wise.')],[PS5,PS5SSD,STORAGE],read=5)

add('best-ps5-ssd-requirements-for-gta-6','PS5 SSD requirements for GTA 6: compatibility checklist','storage',
'Learn the exact M.2 NVMe specification to check before buying an SSD.',
'PS5 supports PCIe Gen4 x4 M.2 NVMe SSDs (Key M), 250 GB–8 TB, with effective heat dissipation. Sony recommends sequential reads of 5,500 MB/s or faster.',
['Choose an M.2 NVMe PCIe Gen4 x4 SSD with Key M; a SATA M.2 drive is not compatible.',
 'Verify a supported length/form factor: 2230, 2242, 2260, 2280 or 22110.',
 'Check it meets Sony’s physical clearance limits, especially if using an attached heatsink.',
 'Use a suitable heatsink/cooling structure and update PS5 system software.',
 'Install according to Sony’s guide, format the drive on PS5, then download/move GTA 6 to it.'],
 [('Can GTA 6 run from a PS5 M.2 SSD?','Yes. Sony supports playing PS5 games directly from compatible M.2 expansion storage.'),('Is 5,500 MB/s mandatory?','Sony recommends 5,500 MB/s or faster; check all listed requirements.'),('Can I install a SATA SSD?','No. Sony does not support M.2 SATA SSDs in the PS5 expansion slot.')],[PS5SSD,STORAGE],read=6,aliases=['ssd extension','ps5 ssd expansion','nvme ps5 5500'])

add('install-ps5-m2-ssd-step-by-step','How to install an M.2 SSD in a PS5 safely','storage',
'A practical installation flow, with safety and compatibility notes.',
'Turn the PS5 off and disconnect power before opening the cover. Use a supported M.2 NVMe drive with heatsink and follow Sony’s illustrated instructions for your model.',
['Update PS5 system software first, then shut down completely and unplug cables.',
 'Discharge static by touching a grounded metal object; do not work with the console running.',
 'Remove the model-specific cover and M.2 expansion-bay cover using Sony’s official guide.',
 'Position the standoff and SSD correctly, seat the drive and secure it without bending the connector.',
 'Replace covers, reconnect, boot the PS5 and format the new M.2 SSD only after confirming it holds no needed data.'],
 [('Will installing an SSD void PS5 warranty?','Sony says the warranty generally should not be affected if you install a compatible drive correctly; damage caused during installation may not be covered.'),('Does the SSD need a heatsink?','Yes, Sony requires effective heat dissipation.'),('Can I play GTA VI from this SSD?','Yes, once the M.2 SSD is recognized and formatted.')],[PS5SSD],read=6)

add('ps5-usb-vs-m2-ssd-gta-6','PS5 USB storage vs M.2 SSD: where can GTA 6 run?','storage',
'A straightforward answer to the most common storage confusion.',
'PS5 games can be stored on USB extended storage, but cannot be played there. To launch GTA VI on PS5, use console storage or a compatible internal M.2 SSD.',
['Use internal PS5 storage for the fastest no-setup option.',
 'Use a compatible M.2 NVMe SSD when you need more playable PS5 game capacity.',
 'Use a USB external drive to archive PS5 games you are not actively playing, then copy them back when needed.',
 'Do not purchase an ordinary external USB SSD expecting GTA VI to launch directly from it.'],
 [('Can GTA 6 play from an external USB SSD on PS5?','No. PS5 games need console storage or a compatible internal M.2 expansion SSD.'),('Can I keep GTA 6 on USB when not playing?','PS5 game files can be moved to USB for storage and moved back before play.'),('Does an M.2 SSD require a separate USB cable?','No. It is installed in the PS5’s internal expansion bay.')],[PS5SSD,STORAGE],read=4)

add('xbox-series-x-s-storage-expansion-gta-6','Xbox Series X|S storage expansion for GTA 6','storage',
'Expansion card versus USB SSD, with Xbox-specific steps.',
'Xbox Series X|S Storage Expansion Cards are designed to play optimized Series X|S games directly. USB HDDs/SSDs can store such games but normally cannot run them without transferring back.',
['Check your console’s My games & apps → Manage → Storage devices view for free space.',
 'Choose a compatible Xbox Series X|S Storage Expansion Card if you need additional playable current-generation storage.',
 'Insert the card in the dedicated expansion slot on the back of the console and configure install location.',
 'Move or install GTA 6 on internal storage or the supported expansion card.',
 'Use ordinary USB storage mainly as an archive for Series X|S optimized games.'],
 [('Can Xbox GTA 6 run from USB?','Optimized Series X|S games generally need internal SSD or a supported Storage Expansion Card for play.'),('Is a PS5 M.2 SSD compatible with Xbox expansion slot?','No. Xbox uses a dedicated storage expansion interface.'),('Can both Xbox Series X and S use the same expansion card?','Yes, Xbox states the expansion cards are compatible with both Series X and Series S.')],[XBOX,'https://www.xbox.com/en-US/accessories/hard-drives/seagate-expansion-card'],read=5,aliases=['console storage expansion','xbox series s storage'])

add('how-to-check-available-storage-ps5-xbox','Check free storage before installing GTA 6','storage',
'A quick PS5 and Xbox storage audit with a 212 GB PS5 target.',
'Open your console’s Storage settings and compare the available capacity with GTA VI’s platform-specific install requirement. PS5’s official preparation guidance is at least 212 GB free.',
['PS5: Settings → Storage → Console Storage; also check M.2 SSD Storage if installed.',
 'Xbox: My games & apps → Manage → Storage devices; inspect available capacity and preferred install device.',
 'Compare your available number to 212 GB on PS5, or the Xbox store/queue size on Xbox.',
 'Free space or install supported expansion storage, then monitor the game download.'],
 [('What if I have only 150 GB free on PS5?','You need at least 62 GB more to meet PlayStation’s stated 212 GB minimum.'),('Will a partially downloaded game need less room?','Do not plan around partial downloads; reserve space for the full game.'),('Should I buy storage immediately?','First identify removable games and your console’s expansion options.')],[PS5,PS5SSD,XBOX],read=3)

add('gta-6-download-stuck-or-slow-ps5','GTA 6 download stuck or slow on PS5: troubleshooting','troubleshooting',
'Check stalled preload, queued downloads, internet and PSN entitlements.',
'First confirm storage and the download queue. Pause and resume the download, check PSN status and network connection, and restart the console normally if it remains stalled.',
['From the PS5 control center open Downloads/Uploads and see whether GTA VI is paused, queued or showing an error code.',
 'Check Settings → Storage and make sure at least the stated required space is available.',
 'Test your internet connection and check PlayStation Network service status.',
 'Pause and resume the download once; if needed restart the PS5 and try a wired network.',
 'If an error code persists, check its exact code in PlayStation support before deleting the installation.'],
 [('Why is GTA 6 queued?','The console may be processing other downloads, waiting for space or awaiting a service response.'),('Should I delete and redownload immediately?','Not as a first step. Check storage, queue and error code first.'),('Does Rest Mode help?','With proper network and update settings, PS5 can keep eligible downloads progressing in Rest Mode.')],[PRELOAD,PS5,PS5SSD],status='PLATFORM GUIDANCE',read=5)

add('gta-6-download-stuck-xbox','GTA 6 download stuck on Xbox: the fix checklist','troubleshooting',
'What to inspect in your Xbox queue before deleting a huge preload.',
'Check Queue status, free storage, Xbox network health and game ownership; prioritize resuming the current download rather than restarting a large install.',
['Open My games & apps → Manage → Queue and identify whether GTA VI is paused or waiting behind another task.',
 'Review storage devices, the installation destination and sufficient free capacity.',
 'Check Xbox service status, home network and connection test; try Ethernet if practical.',
 'Pause/resume the download and restart the console if needed.',
 'Use Xbox support’s guidance for any displayed error code before clearing locally downloaded data.'],
 [('Can I download GTA 6 to any USB drive?','USB may serve as storage, but optimized Series X|S games normally need supported internal/expansion storage to play.'),('Why is the Xbox preload not launching?','Preloading downloads the game; access waits for the official release unlock.'),('Does moving the queue item erase progress?','Changing installations can trigger moves or redownloads; inspect the console prompt before confirming.')],[PRELOAD,XBOX],status='PLATFORM GUIDANCE',read=5)

add('gta-6-not-showing-in-library','GTA 6 not showing in your game library','troubleshooting',
'Find the correct game edition, pre-order entitlement and console account.',
'Confirm the purchase is attached to the account you are signed into, then search the full store library for the correct GTA VI edition and check order history.',
['Verify the account used at checkout or where the digital download code was redeemed.',
 'Search the PlayStation Store / Microsoft Store for Grand Theft Auto VI, not only recent installs.',
 'Review the console’s owned or purchased game library and preorder receipt.',
 'Check regional code compatibility, particularly PlayStation region restrictions.',
 'If the entitlement is missing, contact the original store with your order number.'],
 [('Can I use a PlayStation code from a different region?','Rockstar states PlayStation digital codes can be region-restricted; match the account region.'),('Do Xbox codes have regional restrictions?','Rockstar’s FAQ describes Xbox codes as not region-locked.'),('Does preload require a separate purchase?','It requires an eligible existing preorder or redeemed copy.')],[EDITION,PRELOAD],read=4)

add('gta-6-preload-not-working','GTA 6 preload button missing: what to check','troubleshooting',
'The usual causes: wrong edition, account, region, storage and console update.',
'Rockstar says preload is available. If the button is absent, validate your preorder, software update, account region and library before assuming an outage.',
['Check the right account and the correct GTA VI purchased edition.',
 'Confirm you are on an officially supported PlayStation 5 or Xbox Series X|S.',
 'Check the current system date, console update and network connection.',
 'Look in both Library/Owned Games and the store product page for Install or Download.',
 'Read the Rockstar preload FAQ and platform support before using third-party fixes.'],
 [('Is preload open?','Yes, since November 10, 2026, for eligible purchases.'),('Is GTA 6 available on PS4?','PS4 is not listed among confirmed launch platforms.'),('Can I force an early unlock by changing time zone?','Do not rely on unofficial time-zone bypass claims; use the store and Rockstar unlock guidance.')],[PRELOAD,RELEASE],read=4)

add('gta-6-console-performance-fps','GTA 6 frame rate, 30 FPS and performance modes explained','platforms',
'What Rockstar actually said about console performance, without invented 60 FPS promises.',
'Rockstar stated GTA VI targets 30 frames per second on current-generation consoles. It has not announced a general 60 FPS mode in its November 10 launch briefing.',
['Use 30 FPS as the officially described target at launch, not a promise of 60 or 120 FPS.',
 'Review Rockstar’s PlayStation 5 Pro commentary about visual enhancements instead of conflating resolution with framerate.',
 'Avoid screenshots of unofficial settings menus and “secret FPS unlock” claims until verified from a shipped build.',
 'After launch, distinguish performance measurements from marketing claims.'],
 [('Will GTA 6 have 60 FPS on PS5?','Rockstar’s public prelaunch target is 30 FPS; an official 60 FPS mode was not confirmed in the cited announcement.'),('Does PS5 Pro guarantee 60 FPS?','No. The publicly announced PS5 Pro improvements were visual rather than a confirmed 60 FPS mode.'),('Can my display output 120 Hz?','Some consoles and displays support 120 Hz, but that does not imply GTA 6 will run at 120 FPS.')],[PERFORMANCE,PS5],read=4)

add('gta-6-ps5-pro-vs-ps5','GTA 6 on PS5 Pro vs PS5: verified differences','platforms',
'A practical take on Pro enhancements and what is not promised.',
'Rockstar lists PlayStation 5 Pro improvements including clearer image quality via PSSR and ray-traced shadows available only on PS5 Pro. It still describes a 30 FPS target.',
['If you already own PS5, the base game is supported without a Pro upgrade.',
 'Consider PS5 Pro if visual clarity and supported ray-traced features matter to you.',
 'Do not buy Pro specifically for a rumored 60 FPS mode unless Rockstar confirms it.',
 'Compare official footage and display setup after the game is playable.'],
 [('Can the regular PS5 play GTA 6?','Yes. PlayStation 5 is a confirmed launch platform.'),('What does PS5 Pro add?','Rockstar mentions PSSR image clarity and Pro-only ray-traced shadows.'),('Is 60 FPS confirmed for PS5 Pro?','Not in the Rockstar November 10 announcement.')],[PERFORMANCE,PS5],read=4)

add('gta-6-pc-release-system-requirements','GTA 6 PC release date & system requirements: confirmed status','platforms',
'An evidence-first page about PC launch and why fake spec charts spread.',
'Rockstar’s official November 2026 launch platforms are PlayStation 5 and Xbox Series X|S. No GTA 6 PC launch date or official minimum PC specs have been announced in that listing.',
['Check Rockstar’s GTA VI page for confirmed platforms, rather than a third-party requirements generator.',
 'Treat “minimum RTX/CPU/RAM” tables as estimates unless linked to a Rockstar PC announcement.',
 'Do not download alleged PC cracks, installers or “beta keys”; fake downloads pose security risks.',
 'Bookmark this guide for updates when Rockstar officially announces a PC version.'],
 [('Is GTA 6 on Steam on November 19?','No PC launch is announced in Rockstar’s official platform listing.'),('What GPU do I need for GTA 6 PC?','No official PC minimum or recommended specs are published yet in the cited launch listing.'),('Can I play GTA VI on PS4 or Xbox One?','Those consoles are not included in the official 2026 launch platform announcement.')],[ROCKSTAR,EDITION],read=4,aliases=['gta 6 pc specs','gta 6 steam','gta6 minimum requirements'])

add('can-you-play-gta-6-on-ps4-xbox-one','Can GTA 6 run on PS4 or Xbox One?','platforms',
'Know which console generations are officially supported.',
'No. Rockstar lists PlayStation 5 and Xbox Series X|S as GTA VI launch platforms. PS4 and Xbox One are not in that supported lineup.',
['Read the platform badges on the official GTA VI store page before placing an order.',
 'If you own a PS4 or Xbox One, plan a current-generation console purchase rather than buying an incompatible code.',
 'Use the correct region-specific game store and confirm account eligibility.',
 'Avoid sites claiming “PS4 GTA 6 APK” or unofficial downloads.'],
 [('Can I buy GTA 6 for PS4?','Rockstar does not list a PS4 release.'),('Does Xbox One support GTA 6?','Xbox One is not among the official launch platforms.'),('What Xbox console do I need?','An Xbox Series X or Series S.')],[ROCKSTAR,EDITION],read=3)

add('gta-6-digital-vs-physical-code-in-box','GTA 6 physical vs digital: the code-in-box surprise','platforms',
'Why physical retail packaging does not mean a playable disc in 2026.',
'Rockstar says the GTA VI physical version has a download code in the box, not a game disc. You still need internet, compatible SSD space and code redemption.',
['Check the specific retailer edition description for “code in box” before purchase.',
 'Redeem the included code in the correct PlayStation or Xbox account and region.',
 'Download the full installation to supported console storage; the physical box does not eliminate download requirements.',
 'Keep your receipt and the code secure; do not share the code online.'],
 [('Is there a GTA 6 game disc?','Rockstar’s announced 2026 physical version contains a digital download code rather than a disc.'),('Will it save download space?','No. The full game still needs to be downloaded and installed.'),('Can I sell the game code after redeeming?','A redeemed code is linked to the purchasing account; check store license terms.')],[EDITION,STORE],read=4)

add('gta-6-beginner-preparation-guide','GTA 6 beginner guide: what to do in your first hour','gameplay',
'A spoiler-conscious first-session checklist for controls, objectives, navigation and saving progress.',
'Start with the opening objectives, learn the controls and map interface, test driving and cover, and avoid spending rare resources until the actual in-game economy is clear.',
['Complete the opening tutorial and look for accessibility, subtitles, aim and camera preferences.',
 'Spend a few minutes practicing vehicle handling in a low-stakes area.',
 'Learn the map legend, waypoint controls and how missions are identified before roaming far.',
 'Use manual and automatic save options only as the shipped game presents them; confirm any autosave icon.',
 'For money, vehicles and weapons, wait for verified unlocks and real in-game prices before following tier lists.'],
 [('What should I do first in GTA 6?','Follow the opening objectives, set comfortable controls and familiarize yourself with the map.'),('Should I follow a fast-money trick immediately?','Check its source, version and effect on saved progress before trying it. A beginner session is a good time to learn the normal systems first.'),('Can I use GTASIX while I play?','Yes. Open the mission helper on another screen and choose your current problem to get a checklist without revealing later story events.')],[ROCKSTAR],status='EDITORIAL GUIDANCE',read=5)
articles[-1]['updated']='2026-11-20'

add('gta-6-beginner-driving-tips','GTA 6 driving tips for beginners','gameplay',
'Practical control and camera habits without inventing car stats.',
'Prioritize smooth steering, braking before turns and learning each vehicle’s response. Check the actual game’s controller menu for its button layout.',
['Choose a familiar third-person camera view and comfortable steering sensitivity.',
 'Practice moderate throttle input and slow down before sharp turns.',
 'Try a vehicle you can replace rather than immediately chasing unverified “fastest car” claims.',
 'If vehicle control remains difficult, review the control layout and camera options before changing several settings together.'],
 [('What is the fastest car in GTA 6?','A verified in-game ranking needs controlled testing in the shipped game.'),('Will the driving feel like GTA 5?','Rockstar has not published a complete comparison of handling parameters.'),('Where are the controls?','Pause and open Settings, then Control Scheme. Check the layout displayed for your chosen console and vehicle type.')],[ROCKSTAR,'https://support.rockstargames.com/articles/4jUHNdP22SmaKSF8DWqhXC/how-to-change-grand-theft-auto-vi-settings'],status='EDITORIAL GUIDANCE',read=3)
articles[-1]['updated']='2026-11-20'

add('gta-6-missions-walkthroughs','GTA 6 mission help: find your next objective','gameplay',
'Get a practical next-step plan, choose early mission hints and find a published walkthrough when you need more detail.',
'Use the mission helper to choose what is blocking you, follow a short checklist and reveal hints only for the mission you select. It covers four early missions plus general navigation, driving, controls and progress problems; it is not a complete mission-by-mission walkthrough.',
['Read the current objective exactly as the game displays it. Note the mission name if one is shown.',
 'Open the GTASIX mission helper and choose your console and the problem that best matches your screen.',
 'Follow the first suggested check, then mark the steps you have tried. Reveal a mission hint only when you want more detail.',
 'If your mission is outside the four early missions covered, use the linked published walkthrough directory and search for its exact name.',
 'For a frozen game, crash or missing save, use the technical Help Center before considering a reinstall.'],
 [('Does this site have every GTA 6 mission walkthrough?','No. The helper provides sourced hints for four early missions and general gameplay checklists. A linked editorial directory provides broader coverage.'),('Will I see story spoilers?','Specific hints require selecting a mission and revealing details. Codes are hidden behind separate controls.'),('Can I save a help checklist?','Yes. The mission helper can save your plan on this device when you choose Save plan. It does not synchronize with your game save.'),('Does everyone play missions in one fixed order?','Do not use a directory number as a universal progression order. Some early missions can be attempted in different orders after the opening.')],
[ROCKSTAR,'https://www.videogameschronicle.com/guide/grand-theft-auto-6-complete-walkthrough-hub/','https://www.videogameschronicle.com/guide/gta-6-gear-up-mission-walkthrough/'],status='SOURCE-BASED HELP',read=4,aliases=['stuck in gta 6','what to do next','mission help','mission walkthrough','objective not progressing','first missions'])
articles[-1]['updated']='2026-11-20'

add('gta-6-money-making-guide','GTA 6 money-making methods: what is confirmed?','gameplay',
'A realistic starting point for evaluating payouts, risk and time investment.',
'Before the November 19 release, no trustworthy site can claim exhaustive tested GTA VI money-making payouts. We will rank earning methods by verified money per minute once they can be measured.',
['Ignore unverified “infinite cash glitch” claims and any tool requesting your game account.',
 'When the game launches, note mission or activity name, payout, repeatability and time taken.',
 'Compare earnings by net payout per minute rather than headline reward alone.',
 'Keep a reserve for upgrades and verify whether purchases have meaningful returns.'],
 [('What is the best way to make money in GTA 6?','A reliable ranking requires testing the released game.'),('Are infinite-money glitches real?','Treat prelaunch claims as unverified and potentially unsafe.'),('Will GTA 5 tricks work?','Do not assume GTA 5 mechanics transfer unchanged to GTA 6.')],[ROCKSTAR],status='VERIFY AT LAUNCH',read=3)

add('gta-6-jason-lucia-characters','Jason and Lucia in GTA 6: characters & story','world',
'Meet the protagonists and the setup Rockstar has actually confirmed.',
'Grand Theft Auto VI follows Jason and Lucia in the state of Leonida. Rockstar describes a failed score drawing them into a criminal conspiracy that forces them to rely on each other.',
['Watch the official Launch Trailer for the latest story presentation.',
 'Explore Rockstar’s People & Places page to separate official character biographies from fan theories.',
 'Avoid “ending explained” content posted before release if you prefer a spoiler-free experience.',
 'Use named character profiles as Rockstar confirms more details.'],
 [('Who are the protagonists of GTA 6?','Jason and Lucia.'),('Where does GTA 6 take place?','In Leonida, including Vice City.'),('Is the complete story known?','No. Only released official story materials and previews are confirmed here.')],[ROCKSTAR,TRAILERS],read=4)

add('gta-6-leonida-vice-city-map','GTA 6 Leonida map: Vice City, Keys & known regions','world',
'A spoiler-conscious overview of the official setting and community map caveats.',
'Rockstar confirms the fictional state of Leonida and Vice City. Some fan maps reconstruct landmarks from trailer imagery, but they are not authoritative representations of the final in-game world.',
['Start with Rockstar’s People & Places gallery for confirmed locations and names.',
 'Treat community maps as interpretations of shown footage, not guaranteed road or collectible data.',
 'Use the release build to verify fast-travel, road boundaries and location labels.',
 'Prefer maps that attribute screenshots and label community reconstructions as provisional.'],
 [('Is the full GTA 6 map official yet?','The official public materials describe the setting, but reconstructed fan maps should not be mistaken for a fully validated in-game map.'),('Is Vice City in GTA 6?','Yes. Rockstar explicitly names Vice City.'),('Is Leonida based on Florida?','Leonida and Vice City draw visual inspiration from South Florida; the game world is fictional.')],[ROCKSTAR],read=4)

add('gta-6-soundtrack-and-radio','GTA 6 soundtrack, radio stations & official music','world',
'Know where to find actual confirmed music without fan-made radio lists.',
'Rockstar’s official GTA VI site includes an in-game radio, soundtrack and score section. The Launch Trailer uses an original Justice single, “Flower in a Hurricane.”',
['Listen through Rockstar’s official music and radio hub rather than uncredited uploads.',
 'Use the official video pages to identify music heard in trailers.',
 'Treat circulating “full soundtrack” playlists as unconfirmed unless Rockstar released them.',
 'Keep an eye on official score and album announcements for genuine track listings.'],
 [('What song is in the GTA 6 launch trailer?','Rockstar lists “Flower in a Hurricane” by Justice with featured artists.'),('Is there an official GTA 6 soundtrack?','Rockstar advertises official soundtrack and score material on its game site.'),('Are viral radio playlists official?','Not necessarily; check the source before treating track lists as confirmed.')],[ROCKSTAR,'https://www.rockstargames.com/newswire/article/517572321a549a/watch-the-grand-theft-auto-vi-launch-trailer'],read=4)

add('gta-6-vehicles-best-cars','GTA 6 vehicles: how to spot real stats & best-car claims','world',
'An evidence guide to cars, bikes, boats and aircraft before speed tests are possible.',
'Official trailers show many vehicle types, but reliable top-speed, price, handling and spawn-location rankings require testing the actual game. Trailer identification is not a full stats database.',
['Use the official videos and screenshots as evidence of visual appearances.',
 'Mark each identification as officially named or inferred from footage.',
 'Wait for tested speed and handling measurements before a “fastest cars” ranking.',
 'Cross-check vehicle prices and unlock rules in the released game.'],
 [('What is the fastest GTA 6 car?','No site can verify a comprehensive launch ranking before hands-on tests.'),('Will motorcycles and boats be in GTA 6?','Official footage shows multiple modes of transport; specific vehicle databases need verification.'),('Can we buy every car?','Purchase mechanics and availability must be verified in the game.')],[TRAILERS,ROCKSTAR],status='VERIFY AT LAUNCH',read=4)

add("gta-6-cheat-codes","GTA 6 Cheats: PS5, Xbox Codes and How to Unlock","collectibles","Learn when GTA 6 cheats unlock, PS5 and Xbox reported D-pad codes, and how cheats affect saving and achievements.","PC Gamer and GamesRadar+ report that GTA 6 cheats become available after the main story, with additional challenges for specific codes. They list D-pad combinations including a $250,000 money cheat. GTASIX has not independently tested the inputs. Reporters say cheats disable saving and trophies for the session.",["Complete the main story; launch-day guides say cheats remain locked until then.","Open Pause Menu → Progress → Cheats to see which cheats you have unlocked.","In free roam, open your phone with D-pad Up, then hold L1+R1 on PS5 (LB+RB on Xbox), and enter a code using D-pad directions.","The reported $250,000 cheat is Up, Right, Down, Left, Up, Left, Down, Right, after story completion.","Save your progress first. Cheats reportedly disable saving, trophies and achievements for the active session.","Do not trust sites asking for account passwords, unofficial game installers or cheat-generator downloads."],[["Does GTA 6 have cheats?","Launch-day reviewers report cheats unlocked after completing the main story."],["What is the GTA 6 money cheat?","GamesRadar+ and PC Gamer report Up, Right, Down, Left, Up, Left, Down, Right for $250,000 after completing the story."],["Why don't cheats work?","The main story and the individual challenge must be completed before each cheat is unlocked."],["Do GTA 6 cheats disable saves?","Reviewers report cheats disable saving and achievements while active. Make a backup before using them."],["Did GTASIX test these cheat codes?","No. Inputs are attributed to the original hands-on sources."]],sources=["https://www.pcgamer.com/games/grand-theft-auto/gta-6-cheats-list/","https://www.gamesradar.com/games/grand-theft-auto/gta-6-cheats/","https://www.pushsquare.com/guides/gta-6-cheats-and-unlock-conditions"],status="REPORTED / NOT TESTED",read=6,aliases=["gta 6 cheats","gta 6 money cheat","gta 6 ps5 cheat codes","gta 6 xbox cheat codes"])

add('gta-6-achievements-trophies-100-percent','GTA 6 trophies, achievements & 100% completion','collectibles',
'A completion-planning page that avoids fake final checklists.',
'Final GTA VI trophy/achievement requirements and the exact 100% completion rules should be read from the shipped platform list and in-game completion tracker.',
['Check your platform’s native GTA VI trophies or achievements list after unlock.',
 'Separate story-required tasks from optional collectibles and activities.',
 'Keep a simple personal completion checklist until reliable map pins are available.',
 'For spoiler-sensitive players, hide trophy descriptions where the platform supports it.'],
 [('How many GTA 6 trophies are there?','This site will not claim a final count before verifying the actual platform list.'),('Will GTA 6 need every collectible for 100%?','That depends on actual completion rules, which should be checked at launch.'),('Can cheats disable achievements?','Check shipped-game behavior and warnings before using cheats.')],[ROCKSTAR],status='VERIFY AT LAUNCH',read=3)

add('gta-6-easter-eggs-and-secrets','GTA 6 easter eggs & secrets: verified discovery tracker','collectibles',
'How we will verify real secrets and avoid AI-generated discovery fakes.',
'Treat prelaunch secret-location lists as theories. Valid discoveries need reproducible game footage, location detail and ideally confirmation by multiple players.',
['Collect the discovery’s claimed location and what triggers it.',
 'Check whether the event can be reproduced in an unmodified copy of the game.',
 'Record requirements such as time, weather, mission progress or character.',
 'Only call it “confirmed” with documented evidence; label theories separately.'],
 [('Where are GTA 6 easter eggs?','Reliable in-game maps will be added after release and reproducible verification.'),('Are secret UFO videos official?','Only if the footage is authentic and its game origin is established.'),('Will every GTA 5 secret return?','There is no reason to assume that without game evidence.')],[ROCKSTAR],status='VERIFY AT LAUNCH',read=3)

add('gta-6-trailers-official-videos','All official GTA 6 trailers & gameplay videos','media',
'Watch the official trailers, extended gameplay and preload clip in one place.',
'Rockstar’s official media library features Trailer 1, Trailer 2, An Extended Look, the Launch Trailer and the Pre-Load Now video. The long-form Extended Look was captured from PS5 gameplay footage.',
['Open the Videos library to choose between cinematic trailers and extended gameplay footage.',
 'Prefer embeds or links from Rockstar Games over downloaded reuploads.',
 'Use the publishing date and source label to tell new footage from fan edits.',
 'Read game-specific guide pages for what a scene actually confirms.'],
 [('Is there official GTA 6 gameplay?','Yes. Rockstar released a long-form “An Extended Look” captured from PlayStation 5 footage.'),('Is Trailer 2 real gameplay?','Rockstar says Trailer 2 was captured in-game on PS5 with gameplay and cutscenes.'),('Are all YouTube GTA 6 leaks authentic?','No; use the official Rockstar channel and corroborated sources.')],[TRAILERS,'https://www.rockstargames.com/newswire/article/4k138k8okkk483/grand-theft-auto-vi-an-extended-look-now-playing'],read=4)

add('gta-6-trailer-breakdown-real-vs-rumor','GTA 6 trailer breakdown: confirmed vs speculation','media',
'How to read marketing footage accurately before launch.',
'A trailer can confirm what appears on screen, but does not necessarily prove exact mechanics, mission order, frame rate or whether every scene is free-roam gameplay.',
['Start by identifying the original video, publisher and upload date.',
 'Distinguish explicit Rockstar statements from visual inference.',
 'Check whether a shot is labeled in-game footage, rendered scene or cutscene.',
 'Do not present fan map extrapolations or rumor spreadsheets as official fact.'],
 [('Does every trailer shot prove a playable feature?','No. Even in-game footage can contain scripted or cutscene moments.'),('Where should I watch official GTA 6 videos?','Rockstar’s GTA VI videos library or its verified YouTube channel.'),('Can I trust a “100% leaked mission list”?','Treat it as unverified unless independently supported by the released game.')],[TRAILERS,ROCKSTAR],read=4)

add('how-to-avoid-gta-6-scams-fake-leaks','How to avoid fake GTA 6 downloads, leaks & scams','media',
'Stay safe around fake PC installers, “free keys” and early access streams.',
'Only buy or redeem GTA VI through official storefronts or trusted retail channels. Do not install purported “GTA 6 PC APK” files or share credentials for early access.',
['Check the exact publisher and URL before logging into a store.',
 'Reject “free preload PC” executables while no PC launch is officially announced.',
 'Avoid sites asking for surveys, sideloaded apps, browser extensions or payment card details in exchange for cheat codes.',
 'Use platform support and official game pages to resolve purchases or download errors.'],
 [('Can I download GTA 6 on PC today?','No official PC launch is listed for November 19, 2026.'),('Are GTA 6 APK downloads legitimate?','No official Android GTA VI launch is announced.'),('Where do I buy GTA 6 safely?','Use Rockstar’s official store or your console storefront.')],[ROCKSTAR,STORE],read=4)

# Intents not yet backed by tested gameplay are explicit and avoid fake pages.
# Launch-day guide: Rockstar confirms the settings menus; suggested values are editorial starting points.
add('gta-6-best-settings','Best GTA 6 settings for PS5, PS5 Pro and Xbox','gameplay',
 'Find the best GTA 6 in-game settings for smoother-feeling driving, clearer combat and comfortable play, with an interactive PS5 and Xbox preset builder.',
 'In GTA 6, open Pause Menu → Settings. A useful starting point is Motion Blur Strength 0, Camera Shake Off, Targeting Partial, Aim Assist Strength 4, and comfortable look/aim sensitivity. These are GTASIX recommendations, not an official preset or guaranteed FPS boost. Rockstar targets 30 FPS on consoles.',
 [
 'Open Pause Menu → Settings and review Controller, Gameplay, Display, UI, Camera and Audio. The categories are listed by Rockstar Support.',
 'Under Display, try Motion Blur Strength 0. In Camera → Comfort, turn Camera Shake off and reduce Camera Bob if motion bothers you.',
 'Under Gameplay → Combat, begin with Partial targeting and Aim Assist Strength 4; use Lock-On for more help or Free Aim for a challenge.',
 'In Controller, start with Look and Aim Sensitivity around 7. Test 9 or 10 for look speed only if you feel sluggish. Adjust one step at a time.',
 'Under Gameplay → Movement, test Run for faster on-foot play; for driving, compare a medium or higher vehicle-camera height.',
 'Use UI → Navigation to keep the Minimap visible and UI → Subtitles & Captions to enable readable dialogue if helpful.',
 'Calibrate HDR for your TV, use TV Game Mode, and try the interactive presets on this page. These do not unlock a 60 FPS mode.'
 ],
 [
 ('What are the best GTA 6 settings on PS5?','Start with Motion Blur Strength 0, Camera Shake Off, Targeting Partial, Aim Assist Strength 4 and look/aim sensitivity comfortable to you. Use the settings finder for driving, combat and cinematic profiles.'),
 ('Does GTA 6 have a 60 FPS mode?','Rockstar targets 30 FPS on consoles in its official November 10 update. It did not promise a 60 FPS performance mode. PS5 Pro adds image clarity and ray-traced shadows.'),
 ('Where is aim assist in GTA 6?','Open Pause Menu → Settings → Gameplay → Combat, then change Targeting and Aim Assist Strength.'),
 ('How can I reduce GTA 6 motion sickness?','Try Motion Blur Strength 0, Camera Shake Off, Camera Bob 0–2 and a Persistent Center Dot, then adjust to comfort.'),
 ('Are the settings presets official?','No. The menu categories are documented by Rockstar; GTASIX suggested values are independent, subjective starting points.'),
 ('Are GTA 6 PC graphics settings available?','Rockstar has announced the November 19 launch on PS5 and Xbox Series X|S, not an official PC version or PC graphics options.')
 ],
 sources=['https://support.rockstargames.com/articles/4jUHNdP22SmaKSF8DWqhXC/how-to-change-grand-theft-auto-vi-settings','https://www.rockstargames.com/newswire/article/89834o94713o21/pre-load-grand-theft-auto-vi-now','https://www.gta6map.net/wiki/gta-6/guides/gta-6-settings-and-options'],
 status='CONFIRMED',read=7,
 aliases=['best gta 6 settings ps5','gta 6 xbox settings','gta6 best controller settings','gta 6 aim assist strength','gta 6 motion blur','gta 6 camera settings','gta vi display settings','gta 6 pro graphics','gta 6 settings for driving','gta 6 motion sickness'])

# Sourced GTA VI launch-day search-intent guides, November 19 2026
add("gta-6-how-to-save","How to Save in GTA 6: Manual Save and Autosave","gameplay","Learn where GTA VI saves are, how to use the 15 manual slots and what to do when the Save Game option is unavailable.","Pause with Options (PS5) or Menu (Xbox), choose Game, then Save Game and select a manual save slot. Hands-on reviewers report 15 manual slots and a separate autosave. Save Game is normally unavailable during missions, so return to free roam to save manually.",["Press Options on PS5 or Menu on Xbox to open the pause menu.","Choose Game → Save Game, pick an available slot, and confirm.","Use separate slots for important chapters; do not overwrite your only backup.","Game → Load Game restores a selected save; check the save timestamp first.","If Save Game is greyed out, finish the current mission and retry in free roam.","Autosave is convenient but changes over time. Save manually after longer sessions, particularly before using cheats."],[["How do you save GTA 6?","Pause the game and select Game → Save Game while in free roam."],["How many GTA 6 save slots are there?","Hands-on guides report 15 manual slots and an autosave."],["Why is Save Game greyed out?","Manual saving is unavailable during many missions and early sequences."],["Does GTA 6 autosave?","Yes; use a manual save if you want to preserve a specific point."]],sources=["https://www.pcgamer.com/games/grand-theft-auto/gta-6-save-game/","https://www.powerpyx.com/gta-6-how-to-save/"],status="HANDS-ON REPORTS",read=6,aliases=["gta 6 save game","gta 6 manual save","gta 6 auto save","how to save gta 6","gta 6 save greyed out"])
add("gta-6-how-to-switch-characters","How to Switch Between Jason and Lucia in GTA 6","gameplay","Find the Partner Menu buttons on PlayStation and Xbox and understand the Chapter 2 story restrictions.","After the story unlocks free switching, hold Right on the D-pad and press R1 on PS5 or RB on Xbox Series X|S. Switching is restricted during some missions and early story events.",["Play through the opening; hands-on guides place free character switching in Chapter 2.","During free roam, hold Right on the D-pad to access the Partner Menu.","Press R1 on PS5 or RB on Xbox to switch between Jason and Lucia.","If a character is greyed out, complete your current mission or advance the story.","The Partner Menu can also offer an Invite option; that is different from switching.","Check your Control Scheme if you changed your controller mapping."],[["How do I switch to Lucia on PS5?","Hold Right on the D-pad and press R1 once free switching is unlocked."],["How do I switch on Xbox?","Hold Right on the D-pad and press RB."],["When does character switching unlock?","After progression into Chapter 2, according to multiple launch-day guides."],["Why can I not switch?","Some missions and story sequences temporarily lock the protagonist."]],sources=["https://www.pushsquare.com/guides/gta-6-how-to-change-characters","https://www.gamesradar.com/games/grand-theft-auto/gta-6-switch-characters-command/"],status="HANDS-ON REPORTS",read=6,aliases=["gta6 switch characters","how to switch to lucia","gta 6 partner menu","jason lucia controls","gta 6 xbox character switch"])
add("gta-6-jason-lucia-voice-actors","GTA 6 Voice Actors: Jason Duval, Lucia and Brian","world","Meet the actors behind GTA VI's protagonists and see which roles were publicly confirmed at launch.","Dylan Rourke plays Jason Duval, and Manni L. Perez plays Lucia Caminos. Both acknowledged their roles in a joint public November 19, 2026 statement reported by Video Games Chronicle. Stephen Root has also confirmed involvement as Brian Heder.",["Jason Duval: actor Dylan Rourke publicly acknowledged his GTA VI role in a joint statement on November 19.","Lucia Caminos: Manni L. Perez was also nominated for Best Performance at the 2026 Game Awards.","Brian Heder: Stephen Root confirmed his involvement ahead of release.","Do not treat fan guesses about the other GTA VI characters as confirmed credits.","Consult actor statements, in-game credits or reputable news outlets for new cast announcements."],[["Who voices Jason in GTA 6?","Dylan Rourke, according to a November 19 public confirmation reported by VGC."],["Who voices Lucia in GTA 6?","Manni L. Perez, also a 2026 Game Awards Best Performance nominee."],["Who is the voice of Brian Heder?","Stephen Root."],["Is the entire cast confirmed?","Some main cast members have been publicly identified, but unattributed fan-casting guesses are not confirmation."]],sources=["https://www.videogameschronicle.com/news/see-yall-in-leonida-jasons-actor-finally-confirms-hes-in-gta-6/","https://www.shacknews.com/article/151403/lucia-actor-gta6"],status="CONFIRMED",read=5,aliases=["who voices jason gta 6","dylan rourke gta6","manni l perez lucia","gta 6 voice cast","brian heder stephen root"])
add("gta-6-reviews-scores","GTA 6 Reviews: Metacritic Score and Critical Reception","media","What early GTA 6 critics say about Leonida, the protagonists, and the reported 99/100 Metacritic average.","The Guardian reported that GTA VI held a 99/100 Metacritic critic average on November 19, 2026. Reviews highlight Leonida's detailed world, driving and Jason and Lucia's story. This is a dated snapshot; the score can change as more reviews are counted.",["Check the current Metacritic GTA VI listing; an early score is not permanent.","The Guardian reported a 99/100 Metacritic average on November 19; this guide labels it as a dated snapshot.","Read individual reviews and consider the number of critics included.","Compare impressions of driving, story, exploration and technical stability, not just the headline score.","Avoid spoilers in long reviews if you have not completed the opening chapters.","A critic score does not establish a 60 FPS graphics mode; check official performance information separately."],[["What is GTA 6's Metacritic score?","The Guardian reported 99/100 on November 19, 2026. Check Metacritic for the current number."],["Are GTA 6 reviews positive?","The initial reviews have been overwhelmingly positive, according to major launch-day reporting."],["Does a 99 score mean 60 FPS?","No. Critic scores and frame-rate measurements are different."],["Is GTA 6 out now?","Rockstar announced its PS5 and Xbox Series X|S release on November 19."]],sources=["https://www.theguardian.com/games/2026/nov/19/grand-theft-auto-vi-critics-response-masterpiece","https://www.metacritic.com/game/grand-theft-auto-vi/"],status="DATED REVIEW SNAPSHOT",read=6,aliases=["gta 6 reviews","gta 6 metacritic","gta6 rating","gta vi score","gta 6 critic reviews"])

# November 20 source-backed GTA VI troubleshooting guides.
import json as _issue_json
from pathlib import Path as _IssuePath
for _item in _issue_json.loads((_IssuePath(__file__).with_name("issue_guides.json")).read_text(encoding="utf8")):
    add(_item["slug"], _item["title"], _item["category"], _item["summary"], _item["answer"],
        _item["steps"], _item["faqs"], sources=_item["sources"], status=_item["status"],
        read=_item["read"], aliases=_item["aliases"])

import json as _gameplay_json
from pathlib import Path as _GameplayPath
# Gameplay resources share content, metadata and supplementary sections.
for _guide in _gameplay_json.loads((_GameplayPath(__file__).with_name("gameplay_guides.json")).read_text(encoding="utf8")):
    add(_guide["slug"],_guide["title"],_guide["category"],_guide["summary"],_guide["answer"],_guide["steps"],_guide["faqs"],sources=_guide["sources"],status=_guide["status"],read=_guide["read"],aliases=_guide["aliases"])
    articles[-1]["updated"]="2026-11-20"

roadmap=[
 ('Interactive Leonida map','Pinned locations, collectibles, activities and route filters','At launch, after verifying real coordinates'),
 ('Mission-by-mission guide','Objectives, fail states, reward and no-spoiler toggles','Requires released-game testing'),
 ('Vehicle comparison lab','Handling, 0-60, top speed, price and spawn locations','Requires repeatable measurement'),
 ('Weapon tier lists','Damage, range, cost, recoil and unlocks','Requires repeatable measurement'),
 ('Collectible tracker','Personal progress, map pins and sync options','Requires verified collectible set'),
 ('Save-game troubleshooting','Corrupt save errors, cloud sync and backup safety','Requires actual error cases'),
 ('100% completion roadmap','Required steps, missables and achievement paths','Requires completed game verification'),
 ('Online mode & economy','Sessions, earning and weekly changes','Will publish only with official availability'),
]

videos=[
 dict(title='An Extended Look',sub='Official long-form gameplay presentation',kind='GAMEPLAY',duration='26:48',image='https://i.ytimg.com/vi/tJbzMqJGH4k/maxresdefault.jpg',link='https://www.youtube.com/watch?v=tJbzMqJGH4k',date='AUG 27, 2026',verified='Rockstar Games'),
 dict(title='GTA VI Launch Trailer',sub='A final look at Jason, Lucia and Leonida',kind='OFFICIAL TRAILER',duration='1:29',image=None,link='https://www.rockstargames.com/VI/launch-trailer',date='OCT 15, 2026',verified='Rockstar Games'),
 dict(title='GTA VI Trailer 2',sub='Story, Vice City and PS5-captured footage',kind='OFFICIAL TRAILER',duration='2:47',image='https://i.ytimg.com/vi/VQRLujxTm3c/maxresdefault.jpg',link='https://www.youtube.com/watch?v=VQRLujxTm3c',date='MAY 6, 2025',verified='Rockstar Games'),
 dict(title='GTA VI Trailer 1',sub='The original reveal that started it all',kind='OFFICIAL TRAILER',duration='1:31',image=None,link='https://www.rockstargames.com/videos/rkoCtr1r',date='DEC 2023',verified='Rockstar Games'),
 dict(title='Pre-Load Now',sub='The official launch preparation spot',kind='OFFICIAL UPDATE',duration='0:30',image=None,link='https://www.rockstargames.com/videos/55kss26g',date='NOV 10, 2026',verified='Rockstar Games'),
]
