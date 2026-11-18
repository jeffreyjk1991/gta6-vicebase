"""GTA VI character file: official Rockstar profiles summarized in original language.

As of 2026-11-18 these eight entries are Rockstar's main character profiles.
No unconfirmed voice cast, character deaths, missions or relationship theories.
Artwork is served by Rockstar Games with attribution and a gradient fallback.
"""
SOURCE = 'https://www.rockstargames.com/VI/only-in-leonida'
ART = 'https://www.rockstargames.com/VI/_next/static/media/'
DUO = 'https://media-rockstargames-com.akamaized.net/rockstargames-newsite/img/global/downloads/wallpapers/games/vi/Jason_and_Lucia_01/Jason_and_Lucia_01_landscape.jpg'

CHARACTERS = [
 dict(slug='jason-duval', name='Jason Duval', group='lead', group_label='PROTAGONIST', tagline='THE KEYS NEVER LET GO', region='Leonida Keys', role='Lead character',
      intro='An ex-soldier trying to stay out of trouble, though the drug-running world of the Keys keeps pulling him back.',
      paragraphs=[
          'Jason spent his early years around hustlers and petty criminals. He later joined the Army, hoping to leave that trouble behind.',
          'He is back in the Leonida Keys, working for local drug runners. He stays in property owned by Brian Heder, whose business gives him steady work but little real freedom.',
          'His connection with Lucia is the turning point in the story Rockstar has introduced. Their choices place them at the center of a larger criminal problem across Leonida.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Leonida Keys'),('BACKGROUND','Former Army service'),('TIES','Lucia, Brian, Cal')],connections=['lucia-caminos','brian-heder','cal-hampton'],
      image=DUO,position='68% 50%',theme='coral',image_label='Jason and Lucia official Rockstar artwork',
      evidence='Rockstar introduces Jason as an Army veteran now working for drug runners in the Keys and highlights his relationship with Lucia.',
      unknown='No full mission list, endings, special abilities or confirmed voice actor has been supplied on his Rockstar character profile.'),
 dict(slug='lucia-caminos',name='Lucia Caminos',group='lead',group_label='PROTAGONIST',tagline='A SECOND CHANCE, AT A COST',region='Leonida / formerly Liberty City',role='Lead character',
      intro='Fresh out of prison, Lucia wants a better future and is determined to make the choices that get her there.',
      paragraphs=[
          'Lucia learned how to defend herself growing up. Fighting for her family eventually led to imprisonment at Leonida Penitentiary.',
          'Her mother dreamed of a more comfortable life back when they were in Liberty City. Lucia now wants to build that life by taking a more deliberate approach to risk and opportunity.',
          'Lucia and Jason form the central partnership of GTA VI. Rockstar has described the pair as becoming entangled in trouble after a job goes wrong.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Leonida'),('BACKGROUND','Recently released from prison'),('TIES','Jason Duval')],connections=['jason-duval'],
      image=DUO,position='30% 50%',theme='pink',image_label='Lucia and Jason official Rockstar artwork',
      evidence='Rockstar confirms Lucia served time at Leonida Penitentiary, has family roots in Liberty City and wants to change her future.',
      unknown='Specific character-switching mechanics, a complete backstory and a confirmed actor credit are not established in her official profile.'),
 dict(slug='cal-hampton',name='Cal Hampton',group='underworld',group_label='JASON\'S CIRCLE',tagline='PARANOIA IS A LIFESTYLE',region='Leonida Keys',role='Supporting character',
      intro='Jason\'s friend and fellow Brian Heder associate, more comfortable monitoring Coast Guard communications than chasing a bigger score.',
      paragraphs=[
          'Cal has settled into a low-key life in Leonida. He spends time listening to Coast Guard radio traffic and searching for reasons to distrust the people in charge.',
          'He is friends with Jason and, according to Rockstar, also works within Brian Heder\'s orbit. Their different ambitions hint at tension as Jason starts looking beyond the same routine.',
          'Rockstar frames Cal as a suspicious but familiar presence in Jason\'s life, not as a confirmed playable character.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Leonida / Keys circle'),('BACKGROUND','Brian\'s associate'),('TIES','Jason, Brian')],connections=['jason-duval','brian-heder'],
      image=ART+'Cal_Hampton_landscape.17k7bnt3myg.2.jpg?akim=1&imdensity=1&imwidth=1200',position='center',theme='violet',image_label='Cal Hampton official Rockstar promotional artwork',
      evidence='Rockstar identifies Cal as Jason\'s friend and an associate of Brian, and describes his interest in Coast Guard communications.',
      unknown='No confirmed playable status, voice credit or mission outcomes have been officially disclosed.'),
 dict(slug='brian-heder',name='Brian Heder',group='underworld',group_label='THE KEYS',tagline='OLD-SCHOOL KEYS OPERATOR',region='Leonida Keys',role='Supporting character',
      intro='A veteran smuggler operating through a boatyard, with Jason working for him and staying at one of his properties.',
      paragraphs=[
          'Brian made his name in the Keys during an earlier era of smuggling, and his operation now centers on a boatyard.',
          'He runs the business alongside his third wife, Lori. Rockstar says Brian puts others to work while keeping his own hands relatively clean.',
          'Jason stays in one of Brian\'s properties without rent, but the arrangement comes with work and favors. Cal is also named as an associate of Brian.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Leonida Keys'),('BUSINESS','Boatyard and smuggling'),('TIES','Jason, Cal, Lori')],connections=['jason-duval','cal-hampton'],
      image=ART+'Brian_Heder_landscape.0a-egj5b8yo1q.jpg?akim=1&imdensity=1&imwidth=1200',position='center',theme='teal',image_label='Brian Heder official Rockstar promotional artwork',
      evidence='Rockstar confirms Brian\'s boatyard operations and that Jason stays at one of his properties while helping with local shakedowns.',
      unknown='No confirmed mission rewards, playable role or detailed story ending has been officially disclosed.'),
 dict(slug='raul-bautista',name='Raul Bautista',group='underworld',group_label='THE PROFESSIONAL',tagline='BIG SCORES. BIG RISKS.',region='Leonida',role='Supporting character',
      intro='A charismatic career bank robber who looks for ambitious new talent and keeps increasing the stakes.',
      paragraphs=[
          'Raul is experienced, self-assured and always alert to the next high-value robbery. His profile presents him as a recruiter willing to gamble on capable people.',
          'That appetite for risk can also endanger the people around him. Rockstar suggests his crew eventually faces difficult choices about how far to push their luck.',
          'A confirmed appearance on Rockstar\'s character roster does not establish a particular heist mission, recruitable role or outcome.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Leonida'),('BACKGROUND','Experienced bank robber'),('TIES','Crew not fully detailed')],connections=[],
      image=ART+'Raul_Bautista_landscape.11_3hd0fr69~j.jpg?akim=1&imdensity=1&imwidth=1200',position='center',theme='gold',image_label='Raul Bautista official Rockstar promotional artwork',
      evidence='Rockstar introduces Raul as a seasoned bank robber with a taste for high-risk, high-reward jobs.',
      unknown='His exact relationship to Jason and Lucia, mission list and any playable role are not confirmed by Rockstar.'),
 dict(slug='boobie-ike',name='Boobie Ike',group='music',group_label='VICE CITY POWER PLAYER',tagline='BUILT AN EMPIRE IN VICE CITY',region='Vice City',role='Supporting character',
      intro='A local businessman who has expanded from the streets into real estate, nightlife and a recording operation.',
      paragraphs=[
          'Boobie is established in Vice City, with businesses that stretch across property, a nightclub and a music studio.',
          'His interests are not purely financial: Rockstar highlights his partnership with Dre\'Quan Priest and their plans for Only Raw Records.',
          'The label needs a breakout success, which links Boobie to Dre\'Quan and the hip-hop duo Real Dimez.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Vice City'),('BUSINESS','Property, nightlife, recording'),('TIES','Dre\'Quan Priest')],connections=['dre-quan-priest'],
      image=ART+'Boobie_Ike_landscape.0ldnbn87k-8mq.jpg?akim=1&imdensity=1&imwidth=1200',position='center',theme='coral',image_label='Boobie Ike official Rockstar promotional artwork',
      evidence='Rockstar describes Boobie\'s real estate, club and studio business and his Only Raw Records partnership with Dre\'Quan.',
      unknown='The game has not officially documented every business location, property purchase mechanic or future story outcome.'),
 dict(slug='dre-quan-priest',name="Dre'Quan Priest",group='music',group_label='ONLY RAW RECORDS',tagline='THE NEXT BIG HIT',region='Vice City',role='Supporting character',
      intro='A music entrepreneur whose ambitions are finally moving beyond the club circuit and into a label of his own.',
      paragraphs=[
          'Dre\'Quan has long wanted to succeed in the music business, even when street hustles were paying the bills.',
          'Working with Boobie Ike gave him access to acts and venues. With the duo Real Dimez now signed, he has a reason to aim for much bigger things.',
          'His storyline is presented through the Vice City music scene. Rockstar has not confirmed music-management gameplay systems.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Vice City'),('BUSINESS','Only Raw Records'),('TIES','Boobie, Real Dimez')],connections=['boobie-ike','real-dimez'],
      image=ART+'DreQuan_Priest_landscape.0_b7hszyze6cy.jpg?akim=1&imdensity=1&imwidth=1200',position='center',theme='violet',image_label="Dre'Quan Priest official Rockstar promotional artwork",
      evidence='Rockstar states Dre\'Quan wants a career in music, has worked around Boobie\'s club and has signed Real Dimez.',
      unknown='There is no confirmed playable music-production mode or named voice actor on his official profile.'),
 dict(slug='real-dimez',name='Real Dimez',group='music',group_label='THE DUO',tagline='VIRAL HOOKS. BIG AMBITIONS.',region='Vice City',role='Musical duo: Bae-Luxe and Roxy',
      intro='Rappers Bae-Luxe and Roxy are chasing another breakthrough after early online success and a record-label deal.',
      paragraphs=[
          'Real Dimez is a group, not a single person: the duo consists of longtime friends Bae-Luxe and Roxy.',
          'The two used music and social platforms to build an audience. Rockstar mentions an early track with rapper DWNPLY and a difficult period before their current opportunity.',
          'They are now signed to Only Raw Records, the venture Dre\'Quan Priest is building with support from Boobie Ike.'
      ],facts=[('STATUS','Officially profiled'),('AREA','Vice City'),('MEMBERS','Bae-Luxe and Roxy'),('TIES','Dre\'Quan, Only Raw')],connections=['dre-quan-priest','boobie-ike'],
      image=ART+'Real_Dimez_landscape.0637akp_a5a_q.jpg?akim=1&imdensity=1&imwidth=1200',position='center',theme='pink',image_label='Real Dimez official Rockstar promotional artwork',
      evidence='Rockstar names Bae-Luxe and Roxy as Real Dimez and confirms their connection with Only Raw Records.',
      unknown='Track lists, voice performers and any in-game performance missions are not fully established by official character information.'),
]
BY_SLUG = {c['slug']:c for c in CHARACTERS}
