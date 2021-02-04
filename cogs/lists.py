import importlib
import discord
from discord.ext import commands
import random

beg_people = [
    'Donald Trump',
    'Angelina Jolie',
    'Barack Obama',
    'Elvis Presley',
    'Justin Bieber',
    'Brad Pitt',
    'John F. Kennedy',
    'Ariana Grande',
    'Dwayne Johnson',
    'Abraham Lincoln',
    'Leonardo DiCaprio',
    'Will Smith',
    'Princess Diana',
    'Cyanmaton',
    'Discord',
    'KEA',
    'NatFletch',
    'Spectrum',
    'Drake',
    'Britney Spears',
    'Taylor Swift',
    'Ellen DeGeneres',
    'Elton John',
    'Michael Jackson',
    'John Quincy Adams',
    'James Monroe',
    'James Madison',
    'Thomas Jefferson',
    'John Adams',
    'James K. Polk',
    'Zachary Taylor',
    'Millard Fillmore',
    'William Henry Harrison',
    'John Tyler',
    'Joe Biden',
    'George W. Bush',
    'Bill Clinton',
    'Franklin D. Roosevelt'
]

nou_images = [
    'https://media.discordapp.net/attachments/802185231993405451/805564926234984478/NoU.gif',
    'https://media.discordapp.net/attachments/802185231993405451/805564941687717948/NoU3.gif',
    'https://media.discordapp.net/attachments/802185231993405451/805564938122690590/NoU2.gif'
]

poke_images = [
    'https://media.tenor.com/images/dc5918ea589658e7a958a338839beb34/tenor.gif',
    'https://media.tenor.com/images/897d0c87bee35114aa77f581db66602d/tenor.gif',
    'https://media1.tenor.com/images/d669db4f841de6973c9153e516e9d17c/tenor.gif',
    # 'https://media.tenor.com/images/6c9219ca12bf55106fe9ec1e9d7eaca4/tenor.gif',
    'https://c.tenor.com/yiU1gchHzUQAAAAj/mochi-cute.gif',
    'https://media.tenor.com/images/a0e5105faf3f068bbc545d653b96d019/tenor.gif'
]

slap_images = [
    'https://media.tenor.com/images/e3c933eda0397820d9dcbfef090ec14b/tenor.gif',
    'https://media.tenor.com/images/e61606c524602b99d660851c43ff0599/tenor.gif',
    'https://media.tenor.com/images/bd092fb261df4588a51f9dd1f4815fea/tenor.gif',
    'https://media.tenor.com/images/6dbd997e3e79f21b7841b244833325c0/tenor.gif',
    'https://c.tenor.com/ePDE3ZmpHwcAAAAj/beat-couple.gif'
]

punch_images = [
    'https://media.tenor.com/images/94664693a59fced0a8eebbe7a176753c/tenor.gif',
    'https://media.tenor.com/images/59c8a94055e17ff09be047467dad7efd/tenor.gif',
    'https://c.tenor.com/E85nQHuZqy8AAAAj/fight-punch.gif',
    'https://c.tenor.com/CArnMwDCNPwAAAAj/jinzhan-lily-and-marigold.gif',
    'https://c.tenor.com/lmyPsXjubtoAAAAj/come-fight.gif'
]

sleep_images = [
    'https://tenor.com/view/peach-cat-sleeping-with-you-sleep-goodnight-gif-14541097',
    'https://tenor.com/view/milk-and-mocha-sleeping-good-night-milk-mocha-gif-11453875',
    'https://tenor.com/view/monsters-inc-james-go-to-sleep-gif-6146952',
    'https://tenor.com/view/tonton-friends-sleep-gif-14535339',
    'https://media1.tenor.com/images/65b42ae5359c7dd3f108441b618f8c3e/tenor.gif?itemid=12498624',
    'https://media.tenor.co/videos/54ad3a4a677870362d16880f70ae72c3/mp4'
]

spongebob = [
    'https://tenor.com/view/spongebob-patrick-squidward-head-gif-7230351'
]

wakeup_images = [
    'https://tenor.com/view/darla-wake-up-finding-nemo-shake-why-are-you-sleeping-gif-10149419',
    'https://tenor.com/view/good-morning-funny-animals-insomnia-cat-tired-crazy-cute-gif-11517804',
    'https://tenor.com/view/spongebob-patrick-squidward-head-gif-7230351'
]

_8ballresponses = [
    'As I see it, yes.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don’t count on it.',
    'It is certain.',
    'It is decidedly so.',
    'Most likely.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Outlook good.',
    'Reply hazy, try again.',
    'Signs point to yes.',
    'Very doubtful.',
    'Without a doubt.',
    'Yes.',
    'Yes – definitely.',
    'You may rely on it.'
]

# useless_web = [
#     'https://alwaysjudgeabookbyitscover.com/',
#     'https://weirdorconfusing.com/',
#     'http://www.staggeringbeauty.com/',
#     'https://thatsthefinger.com/',
#     'https://cant-not-tweet-this.com/',
#     'http://corndog.io/',
#     'https://jacksonpollock.org/',
#     'http://www.movenowthinklater.com/',
#     'http://www.partridgegetslucky.com/',
#     'http://burymewithmymoney.com/',
#     'http://beesbeesbees.com/',
#     'https://smashthewalls.com/',
#     'http://eelslap.com/',
#     'http://www.koalastothemax.com/',
#     'http://endless.horse/',
#     'http://www.rrrgggbbb.com/',
#     'http://www.republiquedesmangues.fr/',
#     'https://thezen.zone/',
#     'http://hasthelargehadroncolliderdestroyedtheworldyet.com/',
#     'http://ninjaflex.com/',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     ''
# ]

lenny_faces = [
    '( ͡° ͜ʖ ͡°)',
    'ಠ_ಠ',
    '(▀̿Ĺ̯▀̿ ̿)',
    # '̿'̿'\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿',
    '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)',
    'ʕ•ᴥ•ʔ',
    '(• ε •)',
    '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)',
    '(͡ ͡° ͜ つ ͡͡°)',
    # '(ง'̀- '́)ง',
    '[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]',
    '(ᵔᴥᵔ)',
    '( ͡ᵔ ͜ʖ ͡ᵔ )',
    '◉_◉',
    'ᕦ(ò_óˇ)ᕤ',
    '(｡◕‿◕｡)',
    '(；一_一)',
    '(ʘᗩʘ\')',
    '( ⚆ _ ⚆ )',
    'ಠ‿↼',
    'ಠ~ಠ',
    'Ƹ̵̡Ӝ̵̨̄Ʒ',
    '(･.◤)',
    '¯\_(ツ)_/¯',
    # '̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿',
    '▄︻̷̿┻̿═━一',
    '(▀̿Ĺ̯▀̿ ̿)',
    '༼ つ ◕_◕ ༽つ',
    '(づ｡◕‿‿◕｡)づ',
    '[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]',
    '┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴',
    '( ͡°╭͜ʖ╮͡° )',
    '(ノಠ益ಠ)ノ彡┻━┻',
    '(¬‿¬)',
    # '̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿',
    '(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)',
    '(づ◔ ͜ʖ◔)づ',
    '\ (•◡•) /',
    '(~˘▾˘)~',
    'ᕙ(⇀‸↼‶)ᕗ',
    '˙ ͜ʟ˙',
    '(•ω•)',
    'ಠ⌣ಠ',
    '( ಠ ͜ʖರೃ)',
    "'-_-'",
    '(¬_¬)',
    '╚(ಠ_ಠ)=┐',
    '⌐╦╦═─',
    '¯\(°_o)/¯',
    '°Д°',
    '=U',
    '(͡° ͜ʖ ͡°)'
]

cowboy_sayings = [
    'Don\'t squat with your spurs on.',
    'Don\'t let your yearnings get ahead of your earnings.',
    'Don\'t dig for water under the outhouse.',
    'Don\'t go in if you don\'t know the way out.',
    'Don\'t mess with something that ain\'t bothering you.',
    'Never corner something meaner than you.',
    'Never drive black cattle in the dark.',
    'Never approach a bull from the front, a horse from the rear or a fool from any direction.',
    'Never ask how stupid someone is \'cause they\'ll turn around and show you.',
    'Never ask a barber if you need a haircut.',
    'Never slap a man who\'s chewing tobacco.',
    'I took to the life of a cowboy like a horse takes to oats.',
    'If you climb in the saddle, be ready for the ride.',
    'If you get thrown from a horse, you have to get up and get back on, unless you landed on a cactus; then you have to roll around and scream in pain.',
    'If you haven’t fallen off a horse, then you haven’t been ridin’ long enough.',
    'The horse stopped with a jerk-- and the jerk fell off!',
    'There is no better place to heal a broken heart than on the back of a horse.',
    'There never was a horse that couldn\'t be rode; never was a cowboy who couldn\'t be throwed.',
    'Treat a woman like a racehorse, and she\'ll never be a nag.',
    'When in doubt, let your horse do the thinkin\'.',
    'Speak your mind, but ride a fast horse.',
    '“A cowboy is a man with guts and a horse.” – William James, Western writer',
    '"Every gun makes its own tune.” – Blondie, The Good, The Bad, and the Ugly',
    '“The only healthy way to live life is to learn to like all the little everyday things – like a sip of good whiskey in the evening, a soft bed, a glass of buttermilk, or a feisty gentleman like myself.” – Gus McCrae, Lonesome Dove by Larry McMurtry',
    '"I won\t be wronged, I won\'t be insulted, and I won\'t be laid a hand on. I don\'t do these things to other people, and I require the same from them." – J.B. Books, The Shootist',
    '“I’m your huckleberry.” Doc Holliday, Tombstone',
    '“Shootin’ from ambush is a bad habit. You may not live long enough to outgrow it.” – Hopalong Cassidy, Hopalong Cassidy: Lawless Legacy',
    '"Snakes like you usually die of their own poison." – Chris Morrell, ‘Neath the Arizona Skies'
]

roasts = [
    'You\'re the reason the gene pool needs a lifeguard.',
    'You\'re as useless as the "ueue" in "queue".',
    'Mirrors can\'t talk. Luckily for you, they can\'t laugh either.',
    'If I had a face like yours I\'d sue my parents.',
    'Someday you\'ll go far, and I hope you stay there.',
    'You must have been born on a highway cos\' that\'s where most accidents happen.',
    'If laughter is the best medicine, your face must be curing the world.',
    'I\'m glad to see you\'re not letting your education get in the way of your ignorance.',
    'So, a thought crossed your mind? Must have been a long and lonely journey.',
    'If I wanted to kill myself I\'d climb your ego and jump to your IQ.',
    'If I wanted to know the lowest number I\'d climb your ego and jump to your IQ.',
    'I\'d agree with you but then we\'d both be wrong.',
    'When I see your face there\'s not a thing I would change... except the direction I was walking in.',
    'If I had a dollar for every time you said something smart I\'d be broke.',
    'When you were born the doctor threw you out the window and the window threw you back.',
    'I’m jealous of people who don’t know you.',
    'I’d smack you, but that would be animal abuse.',
    'You sound reasonable… Time to up my medication.',
    'I might be crazy, but crazy is better than stupid.',
    '90%\ of your ‘beauty’ could be removed with a Kleenex.',
    'Some people should use a glue stick instead of chapstick.'
    'It’s scary to think people like you are allowed to vote.',
    'Keep rolling your eyes. Maybe you’ll find your brain back there.',
    'I suggest you do a little soul searching. You might just find one.',
    'Everyone brings happiness to a room. I do when I enter, you do when you leave.',
    'I thought I had the flu, but then I realized your face makes me sick to my stomach.',
    'When karma comes back to punch you in the face, I want to be there in case it needs help.',
    'I keep thinking you can’t get any dumber and you keep proving me wrong.',
    'These roasts come from: https://humoropedia.com/best-comebacks-n-funny-insults/, https://www.scarymommy.com/best-insults-and-comebacks/, https://www.scoopwhoop.com/best-smartass-insults/, and https://humoropedia.com/most-savage-roasts-n-jokes-list/!'
]
numbers = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0'
]

letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]
# colours = Tuple[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]:

# colours = [
# Tuple[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]:
# random.choice(numbers, letters), random.choice(numbers, letters), random.choice(numbers, letters), random.choice(numbers, letters), random.choice(numbers, letters), random.choice(numbers, letters)
# 0x00FFFF,
# 0x00008B,
# 0x000080,
# 0x0000CD,
# 0x0000FF,
# 0xFF0000,
# 0x800000,
# 0xFFFF00,
# 0x00FF00,
# 0x999999,
# 0x454545,
# 0x000000,
# 0x800080,
# 0x4B0082,
# 0x9932CC,
# 0x8B008B,
# 0x00FF00,
# 0x228B22,
# 0x008000,
# 0x006400,
# 0xC0C0C0,
# 0xFFD700,
# 0xFFA500,
# 0xFF8C00,
# 0xFF7F50,
# 0xFF6347,
# 0xFFC0CB,
# 0xFFB6C1,
# # 0xFF69B4,
# 0xFF1493
# ]

# colour = discord.Colour.from_hsv(random.random(), 1, 255)
colour = random.randint(0, 16777216)

# From https://www.scoopwhoop.com/best-smartass-insults/
