#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Thu May 25 12:09:38 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'accent2'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ajnafannikertesz/Desktop/Accents /accent2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

#initialize keyboard image components
keyimage = visual.ImageStim(
    win=win,
    name='keyimage', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

keyimage.setImage('/Users/ajnafannikertesz/Desktop/Accents /leftrightim.png')

# --- Initialize components for Routine "Welcome" ---
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='Welcome to the study!\n\nThis study has two parts. In the first part you will have to categorize words upon hearing them, while in the second part you will listen and make judgments about short passages.  \n\n\nPress SPACE to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Part1" ---
p1_instructions = visual.TextStim(win=win, name='p1_instructions',
    text='Part 1\n\nIn this first part of the study you will hear words that are either living or non-living things. For living things press the left key and for non-living things press the right key. This is a study measuring response time, so try to be as fast as possible.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "words" ---
word_resp = keyboard.Keyboard()
wordlist = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='wordlist')
wordlist.setVolume(1.0)

# --- Initialize components for Routine "Part2" ---
p2_instructions = visual.TextStim(win=win, name='p2_instructions',
    text='Part 2\n\nIn this part of the study you will hear three brief passages. After listening to each passage you will be asked several questions about the content and your impressions of it.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "passages" ---
passagelist = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='passagelist')
passagelist.setVolume(1.0)
belive = visual.Slider(win=win, name='belive',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
nice = visual.Slider(win=win, name='nice',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
smart = visual.Slider(win=win, name='smart',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)
trustworthy = visual.Slider(win=win, name='trustworthy',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-4, readOnly=False)

# --- Initialize components for Routine "samples" ---
sample_sounds = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sample_sounds')
sample_sounds.setVolume(1.0)
origin = visual.TextStim(win=win, name='origin',
    text='Where do you think this speaker is from?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
first_lang = visual.TextStim(win=win, name='first_lang',
    text="What do you think is this speaker's first langauge?",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
recognize = visual.TextStim(win=win, name='recognize',
    text='Do you recognize this speaker?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "thankyou" ---
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Thank you for your participation. Your responses have been recorded.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Welcome_text, key_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome_text.started')
        Welcome_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Part1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Part1Components = [p1_instructions, key_resp_2]
for thisComponent in Part1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Part1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *p1_instructions* updates
    if p1_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p1_instructions.frameNStart = frameN  # exact frame index
        p1_instructions.tStart = t  # local t and not account for scr refresh
        p1_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p1_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'p1_instructions.started')
        p1_instructions.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Part1" ---
for thisComponent in Part1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Part1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('words.xlsx'),
    seed=None, name='trials')
    
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

# read in all words we need to see
all_words = [
    "shellfish",
    "bloodhound",
    "antelope",
    "woodpecker",
    "swordfish",
    "walrus",
    "tortoise",
    "caterpillar",
    "piranha",
    "chimpanzee",
    "gazelle",
    "seagull",
    "catfish",
    "critter",
    "giraffe",
    "ferret",
    "rattlesnake",
    "octopus",
    "livestock",
    "beetle",
    "possum",
    "rhino",
    "panda",
    "hamster",
    "crocodile",
    "kangaroo",
    "corral",
    "parasite",
    "zebra",
    "predator",
    "scorpion",
    "dolphin",
    "cricket",
    "penguin",
    "cuckoo",
    "fiancee",
    "bacteria",
    "goldfish",
    "oyster",
    "insect",
    "parrot",
    "reindeer",
    "kitten",
    "camel",
    "donkey",
    "butterfly",
    "lion",
    "salmon",
    "tuna",
    "spider",
    "elephant",
    "goose",
    "tiger",
    "mouse",
    "rabbit",
    "snake",
    "turkey",
    "flower",
    "grandmother",
    "monkey",
    "musket",
    "sunscreen",
    "sauerkraut",
    "matchbook",
    "eyeliner",
    "aftershave",
    "corkscrew",
    "airstrip",
    "fragrance",
    "scrapbook",
    "buttermilk",
    "racquetball",
    "podium",
    "duffel",
    "eggnog",
    "folder",
    "armour",
    "syringe",
    "manicure",
    "washer",
    "espresso",
    "email",
    "barbershop",
    "uranium",
    "softball",
    "bleach",
    "vocabulary",
    "gadget",
    "grapefruit",
    "plaster",
    "hydrogen",
    "aquarium",
    "boiler",
    "pager",
    "jewellery",
    "mainland",
    "cinnamon",
    "fiber",
    "bagel",
    "casket",
    "telegraph",
    "laptop",
    "yearbook",
    "toothbrush",
    "playground",
    "freezer",
    "freeway",
    "makeup",
    "arrow",
    "dynamite",
    "photograph",
    "missile",
    "basket",
    "museum",
    "palace",
    "diamond",
    "butter",
    "wallet",
    "garage",
    "pizza"
]
keyimage.autoDraw = True
for thisTrial in trials:
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    # check if the word has been said yet
    if target in all_words:
        # remove from list
        all_words.remove(target)
    else:
        # otherwise, skip this trial
        continue

    currentLoop = trials

    
    
    # --- Prepare to start Routine "words" ---
    continueRoutine = True
    routineForceEnded = False

    # update component parameters for each repeat
    word_resp.keys = []
    word_resp.rt = []
    _word_resp_allKeys = []

    wordlist.setSound(wordfile, hamming=True)
    wordlist.setVolume(1.0, log=False)

    # keep track of which components have finished
    wordsComponents = [word_resp, wordlist]
    for thisComponent in wordsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "words" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_resp* updates
        waitOnFlip = False
        if word_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word_resp.frameNStart = frameN  # exact frame index
            word_resp.tStart = t  # local t and not account for scr refresh
            word_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'word_resp.started')
            word_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(word_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(word_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if word_resp.status == STARTED and not waitOnFlip:
            theseKeys = word_resp.getKeys(keyList=['right', 'left'], waitRelease=False)
            _word_resp_allKeys.extend(theseKeys)
            if len(_word_resp_allKeys):
                word_resp.keys = _word_resp_allKeys[-1].name  # just the last key pressed
                word_resp.rt = _word_resp_allKeys[-1].rt
                # was this correct?
                if (word_resp.keys == str(correct)) or (word_resp.keys == correct):
                    word_resp.corr = 1
                else:
                    word_resp.corr = 0
                if str(word_resp.keys) in ['right','left']:
                    word_resp.status = FINISHED
                    wordlist.status = FINISHED
        # start/stop wordlist
        if wordlist.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wordlist.frameNStart = frameN  # exact frame index
            wordlist.tStart = t  # local t and not account for scr refresh
            wordlist.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('wordlist.started', tThisFlipGlobal)
            wordlist.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wordsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "words" ---
    for thisComponent in wordsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if word_resp.keys in ['', [], None]:  # No response was made
        word_resp.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           word_resp.corr = 1;  # correct non-response
        else:
           word_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('word_resp.keys',word_resp.keys)
    trials.addData('word_resp.corr', word_resp.corr)
    if word_resp.keys != None:  # we had a response
        trials.addData('word_resp.rt', word_resp.rt)
    wordlist.stop()  # ensure sound has stopped at end of routine
    # the Routine "words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'
keyimage.clearTextures()

'''
# --- Prepare to start Routine "Part2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Part2Components = [p2_instructions, key_resp_3]
for thisComponent in Part2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Part2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *p2_instructions* updates
    if p2_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p2_instructions.frameNStart = frameN  # exact frame index
        p2_instructions.tStart = t  # local t and not account for scr refresh
        p2_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p2_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'p2_instructions.started')
        p2_instructions.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Part2" ---
for thisComponent in Part2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Part2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('passages.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "passages" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    passagelist.setSound('passages.xlsx', hamming=True)
    passagelist.setVolume(1.0, log=False)
    belive.reset()
    nice.reset()
    smart.reset()
    trustworthy.reset()
    # keep track of which components have finished
    passagesComponents = [passagelist, belive, nice, smart, trustworthy]
    for thisComponent in passagesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "passages" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop passagelist
        if passagelist.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            passagelist.frameNStart = frameN  # exact frame index
            passagelist.tStart = t  # local t and not account for scr refresh
            passagelist.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('passagelist.started', tThisFlipGlobal)
            passagelist.play(when=win)  # sync with win flip
        
        # *belive* updates
        if belive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            belive.frameNStart = frameN  # exact frame index
            belive.tStart = t  # local t and not account for scr refresh
            belive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(belive, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'belive.started')
            belive.setAutoDraw(True)
        
        # Check belive for response to end routine
        if belive.getRating() is not None and belive.status == STARTED:
            continueRoutine = False
        
        # *nice* updates
        if nice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nice.frameNStart = frameN  # exact frame index
            nice.tStart = t  # local t and not account for scr refresh
            nice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nice.started')
            nice.setAutoDraw(True)
        
        # Check nice for response to end routine
        if nice.getRating() is not None and nice.status == STARTED:
            continueRoutine = False
        
        # *smart* updates
        if smart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smart.frameNStart = frameN  # exact frame index
            smart.tStart = t  # local t and not account for scr refresh
            smart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smart.started')
            smart.setAutoDraw(True)
        
        # Check smart for response to end routine
        if smart.getRating() is not None and smart.status == STARTED:
            continueRoutine = False
        
        # *trustworthy* updates
        if trustworthy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trustworthy.frameNStart = frameN  # exact frame index
            trustworthy.tStart = t  # local t and not account for scr refresh
            trustworthy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trustworthy, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trustworthy.started')
            trustworthy.setAutoDraw(True)
        
        # Check trustworthy for response to end routine
        if trustworthy.getRating() is not None and trustworthy.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in passagesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "passages" ---
    for thisComponent in passagesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    passagelist.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('belive.response', belive.getRating())
    trials_2.addData('belive.rt', belive.getRT())
    trials_2.addData('nice.response', nice.getRating())
    trials_2.addData('nice.rt', nice.getRT())
    trials_2.addData('smart.response', smart.getRating())
    trials_2.addData('smart.rt', smart.getRT())
    trials_2.addData('trustworthy.response', trustworthy.getRating())
    trials_2.addData('trustworthy.rt', trustworthy.getRT())
    # the Routine "passages" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('samples/samples.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "samples" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sample_sounds.setSound('samples/samples.xlsx', hamming=True)
    sample_sounds.setVolume(1.0, log=False)
    # keep track of which components have finished
    samplesComponents = [sample_sounds, origin, first_lang, recognize]
    for thisComponent in samplesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "samples" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sample_sounds
        if sample_sounds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sample_sounds.frameNStart = frameN  # exact frame index
            sample_sounds.tStart = t  # local t and not account for scr refresh
            sample_sounds.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sample_sounds.started', tThisFlipGlobal)
            sample_sounds.play(when=win)  # sync with win flip
        
        # *origin* updates
        if origin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            origin.frameNStart = frameN  # exact frame index
            origin.tStart = t  # local t and not account for scr refresh
            origin.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(origin, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'origin.started')
            origin.setAutoDraw(True)
        
        # *first_lang* updates
        if first_lang.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_lang.frameNStart = frameN  # exact frame index
            first_lang.tStart = t  # local t and not account for scr refresh
            first_lang.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_lang, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'first_lang.started')
            first_lang.setAutoDraw(True)
        if first_lang.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > first_lang.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                first_lang.tStop = t  # not accounting for scr refresh
                first_lang.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'first_lang.stopped')
                first_lang.setAutoDraw(False)
        
        # *recognize* updates
        if recognize.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognize.frameNStart = frameN  # exact frame index
            recognize.tStart = t  # local t and not account for scr refresh
            recognize.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognize, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recognize.started')
            recognize.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in samplesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "samples" ---
    for thisComponent in samplesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sample_sounds.stop()  # ensure sound has stopped at end of routine
    # the Routine "samples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'

'''
# --- Prepare to start Routine "thankyou" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
thankyouComponents = [thank_you]
for thisComponent in thankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thankyou" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you.started')
        thank_you.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thankyou" ---
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
