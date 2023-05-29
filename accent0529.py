#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on Mon May 29 13:19:03 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
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
psychopyVersion = '2023.1.2'
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
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
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
    text='Part 1\n\nIn this first part of the study you will hear words that are either living or non-living things. For living things press "A" and for non-living things press "L". This is a study measuring response time, so try to be as fast as possible. If you make an error you can correct yourself and the button you pressed last will be recorded.',
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
text_believe = visual.TextStim(win=win, name='text_believe',
    text='To what extent do you think this presentation was believable?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
believe = visual.Slider(win=win, name='believe',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=("Not at all believable", "Highly believable"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
mouse_believe = event.Mouse(win=win)
x, y = [None, None]
mouse_believe.mouseClock = core.Clock()
text_nice = visual.TextStim(win=win, name='text_nice',
    text='How nice do you think this person is?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
nice = visual.Slider(win=win, name='nice',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=("Not at all nice", "Very nice"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-5, readOnly=False)
mouse_nice = event.Mouse(win=win)
x, y = [None, None]
mouse_nice.mouseClock = core.Clock()
text_smart = visual.TextStim(win=win, name='text_smart',
    text='How smart do you think this person is?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
smart = visual.Slider(win=win, name='smart',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=("Not at all smart", "Very smart"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-8, readOnly=False)
mouse_smart = event.Mouse(win=win)
x, y = [None, None]
mouse_smart.mouseClock = core.Clock()
text_trust = visual.TextStim(win=win, name='text_trust',
    text='How trustworthy do you think this person is?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
trust = visual.Slider(win=win, name='trust',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=("Not at all trustworthy", "Very trustworthy"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-11, readOnly=False)
mouse_trust = event.Mouse(win=win)
x, y = [None, None]
mouse_trust.mouseClock = core.Clock()
key_resp_next = keyboard.Keyboard()

# --- Initialize components for Routine "samples" ---
sample_sounds = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sample_sounds')
sample_sounds.setVolume(1.0)
textbox_origin = visual.TextBox2(
     win, text=None, placeholder='Where do you think this person is from?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_origin',
     depth=-1, autoLog=True,
)
textbox_firstlang = visual.TextBox2(
     win, text=None, placeholder='What do you think is this person’s first language?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_firstlang',
     depth=-2, autoLog=True,
)
recognize = visual.TextStim(win=win, name='recognize',
    text='Do you recognize this speaker?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_recognize = visual.Slider(win=win, name='slider_recognize',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-4, readOnly=False)
end_button = visual.ButtonStim(win, 
    text='Click here to continue', font='Arvo',
    pos=(0, 0),
    letterHeight=0.05,
    size=(0.5, 0.5), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='end_button',
    depth=-5
)
end_button.buttonClock = core.Clock()

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
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    
    # if Welcome_text is starting this frame...
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome_text.started')
        # update status
        Welcome_text.status = STARTED
        Welcome_text.setAutoDraw(True)
    
    # if Welcome_text is active this frame...
    if Welcome_text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
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
        if eyetracker:
            eyetracker.setConnectionState(False)
    
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
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *p1_instructions* updates
    
    # if p1_instructions is starting this frame...
    if p1_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p1_instructions.frameNStart = frameN  # exact frame index
        p1_instructions.tStart = t  # local t and not account for scr refresh
        p1_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p1_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'p1_instructions.started')
        # update status
        p1_instructions.status = STARTED
        p1_instructions.setAutoDraw(True)
    
    # if p1_instructions is active this frame...
    if p1_instructions.status == STARTED:
        # update params
        pass
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
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
        if eyetracker:
            eyetracker.setConnectionState(False)
    
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

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "words" ---
    continueRoutine = True
    # update component parameters for each repeat
    word_resp.keys = []
    word_resp.rt = []
    _word_resp_allKeys = []
    wordlist.setSound('words.xlsx', hamming=True)
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_resp* updates
        waitOnFlip = False
        
        # if word_resp is starting this frame...
        if word_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word_resp.frameNStart = frameN  # exact frame index
            word_resp.tStart = t  # local t and not account for scr refresh
            word_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'word_resp.started')
            # update status
            word_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(word_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(word_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if word_resp.status == STARTED and not waitOnFlip:
            theseKeys = word_resp.getKeys(keyList=['a', 'l'], waitRelease=False)
            _word_resp_allKeys.extend(theseKeys)
            if len(_word_resp_allKeys):
                word_resp.keys = _word_resp_allKeys[-1].name  # just the last key pressed
                word_resp.rt = _word_resp_allKeys[-1].rt
                # was this correct?
                if (word_resp.keys == str(correct)) or (word_resp.keys == correct):
                    word_resp.corr = 1
                else:
                    word_resp.corr = 0
        
        # if wordlist is starting this frame...
        if wordlist.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wordlist.frameNStart = frameN  # exact frame index
            wordlist.tStart = t  # local t and not account for scr refresh
            wordlist.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('wordlist.started', tThisFlipGlobal)
            # update status
            wordlist.status = STARTED
            wordlist.play(when=win)  # sync with win flip
        # update wordlist status according to whether it's playing
        if wordlist.isPlaying:
            wordlist.status = STARTED
        elif wordlist.isFinished:
            wordlist.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
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


# --- Prepare to start Routine "Part2" ---
continueRoutine = True
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
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *p2_instructions* updates
    
    # if p2_instructions is starting this frame...
    if p2_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p2_instructions.frameNStart = frameN  # exact frame index
        p2_instructions.tStart = t  # local t and not account for scr refresh
        p2_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p2_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'p2_instructions.started')
        # update status
        p2_instructions.status = STARTED
        p2_instructions.setAutoDraw(True)
    
    # if p2_instructions is active this frame...
    if p2_instructions.status == STARTED:
        # update params
        pass
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
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
        if eyetracker:
            eyetracker.setConnectionState(False)
    
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
    # update component parameters for each repeat
    passagelist.setSound('passages.xlsx', hamming=True)
    passagelist.setVolume(1.0, log=False)
    believe.reset()
    # setup some python lists for storing info about the mouse_believe
    mouse_believe.x = []
    mouse_believe.y = []
    mouse_believe.leftButton = []
    mouse_believe.midButton = []
    mouse_believe.rightButton = []
    mouse_believe.time = []
    mouse_believe.clicked_name = []
    gotValidClick = False  # until a click is received
    nice.reset()
    # setup some python lists for storing info about the mouse_nice
    mouse_nice.x = []
    mouse_nice.y = []
    mouse_nice.leftButton = []
    mouse_nice.midButton = []
    mouse_nice.rightButton = []
    mouse_nice.time = []
    mouse_nice.clicked_name = []
    gotValidClick = False  # until a click is received
    smart.reset()
    # setup some python lists for storing info about the mouse_smart
    mouse_smart.x = []
    mouse_smart.y = []
    mouse_smart.leftButton = []
    mouse_smart.midButton = []
    mouse_smart.rightButton = []
    mouse_smart.time = []
    mouse_smart.clicked_name = []
    gotValidClick = False  # until a click is received
    trust.reset()
    # setup some python lists for storing info about the mouse_trust
    mouse_trust.x = []
    mouse_trust.y = []
    mouse_trust.leftButton = []
    mouse_trust.midButton = []
    mouse_trust.rightButton = []
    mouse_trust.time = []
    mouse_trust.clicked_name = []
    gotValidClick = False  # until a click is received
    key_resp_next.keys = []
    key_resp_next.rt = []
    _key_resp_next_allKeys = []
    # keep track of which components have finished
    passagesComponents = [passagelist, text_believe, believe, mouse_believe, text_nice, nice, mouse_nice, text_smart, smart, mouse_smart, text_trust, trust, mouse_trust, key_resp_next]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if passagelist is starting this frame...
        if passagelist.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            passagelist.frameNStart = frameN  # exact frame index
            passagelist.tStart = t  # local t and not account for scr refresh
            passagelist.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('passagelist.started', tThisFlipGlobal)
            # update status
            passagelist.status = STARTED
            passagelist.play(when=win)  # sync with win flip
        # update passagelist status according to whether it's playing
        if passagelist.isPlaying:
            passagelist.status = STARTED
        elif passagelist.isFinished:
            passagelist.status = FINISHED
        
        # *text_believe* updates
        
        # if text_believe is starting this frame...
        if text_believe.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_believe.frameNStart = frameN  # exact frame index
            text_believe.tStart = t  # local t and not account for scr refresh
            text_believe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_believe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_believe.started')
            # update status
            text_believe.status = STARTED
            text_believe.setAutoDraw(True)
        
        # if text_believe is active this frame...
        if text_believe.status == STARTED:
            # update params
            pass
        
        # *believe* updates
        
        # if believe is starting this frame...
        if believe.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            believe.frameNStart = frameN  # exact frame index
            believe.tStart = t  # local t and not account for scr refresh
            believe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(believe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'believe.started')
            # update status
            believe.status = STARTED
            believe.setAutoDraw(True)
        
        # if believe is active this frame...
        if believe.status == STARTED:
            # update params
            pass
        # *mouse_believe* updates
        
        # if mouse_believe is starting this frame...
        if mouse_believe.status == NOT_STARTED and t >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_believe.frameNStart = frameN  # exact frame index
            mouse_believe.tStart = t  # local t and not account for scr refresh
            mouse_believe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_believe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_believe.started', t)
            # update status
            mouse_believe.status = STARTED
            mouse_believe.mouseClock.reset()
            prevButtonState = mouse_believe.getPressed()  # if button is down already this ISN'T a new click
        if mouse_believe.status == STARTED:  # only update if started and not finished!
            buttons = mouse_believe.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(believe, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_believe):
                            gotValidClick = True
                            mouse_believe.clicked_name.append(obj.name)
                    x, y = mouse_believe.getPos()
                    mouse_believe.x.append(x)
                    mouse_believe.y.append(y)
                    buttons = mouse_believe.getPressed()
                    mouse_believe.leftButton.append(buttons[0])
                    mouse_believe.midButton.append(buttons[1])
                    mouse_believe.rightButton.append(buttons[2])
                    mouse_believe.time.append(mouse_believe.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *text_nice* updates
        
        # if text_nice is starting this frame...
        if text_nice.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_nice.frameNStart = frameN  # exact frame index
            text_nice.tStart = t  # local t and not account for scr refresh
            text_nice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_nice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_nice.started')
            # update status
            text_nice.status = STARTED
            text_nice.setAutoDraw(True)
        
        # if text_nice is active this frame...
        if text_nice.status == STARTED:
            # update params
            pass
        
        # *nice* updates
        
        # if nice is starting this frame...
        if nice.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
            # keep track of start time/frame for later
            nice.frameNStart = frameN  # exact frame index
            nice.tStart = t  # local t and not account for scr refresh
            nice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nice.started')
            # update status
            nice.status = STARTED
            nice.setAutoDraw(True)
        
        # if nice is active this frame...
        if nice.status == STARTED:
            # update params
            pass
        # *mouse_nice* updates
        
        # if mouse_nice is starting this frame...
        if mouse_nice.status == NOT_STARTED and t >= 60-frameTolerance:
            # keep track of start time/frame for later
            mouse_nice.frameNStart = frameN  # exact frame index
            mouse_nice.tStart = t  # local t and not account for scr refresh
            mouse_nice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_nice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_nice.started', t)
            # update status
            mouse_nice.status = STARTED
            mouse_nice.mouseClock.reset()
            prevButtonState = mouse_nice.getPressed()  # if button is down already this ISN'T a new click
        if mouse_nice.status == STARTED:  # only update if started and not finished!
            buttons = mouse_nice.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(nice, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_nice):
                            gotValidClick = True
                            mouse_nice.clicked_name.append(obj.name)
                    x, y = mouse_nice.getPos()
                    mouse_nice.x.append(x)
                    mouse_nice.y.append(y)
                    buttons = mouse_nice.getPressed()
                    mouse_nice.leftButton.append(buttons[0])
                    mouse_nice.midButton.append(buttons[1])
                    mouse_nice.rightButton.append(buttons[2])
                    mouse_nice.time.append(mouse_nice.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *text_smart* updates
        
        # if text_smart is starting this frame...
        if text_smart.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_smart.frameNStart = frameN  # exact frame index
            text_smart.tStart = t  # local t and not account for scr refresh
            text_smart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_smart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_smart.started')
            # update status
            text_smart.status = STARTED
            text_smart.setAutoDraw(True)
        
        # if text_smart is active this frame...
        if text_smart.status == STARTED:
            # update params
            pass
        
        # *smart* updates
        
        # if smart is starting this frame...
        if smart.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            smart.frameNStart = frameN  # exact frame index
            smart.tStart = t  # local t and not account for scr refresh
            smart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smart.started')
            # update status
            smart.status = STARTED
            smart.setAutoDraw(True)
        
        # if smart is active this frame...
        if smart.status == STARTED:
            # update params
            pass
        # *mouse_smart* updates
        
        # if mouse_smart is starting this frame...
        if mouse_smart.status == NOT_STARTED and t >= 60-frameTolerance:
            # keep track of start time/frame for later
            mouse_smart.frameNStart = frameN  # exact frame index
            mouse_smart.tStart = t  # local t and not account for scr refresh
            mouse_smart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_smart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_smart.started', t)
            # update status
            mouse_smart.status = STARTED
            mouse_smart.mouseClock.reset()
            prevButtonState = mouse_smart.getPressed()  # if button is down already this ISN'T a new click
        if mouse_smart.status == STARTED:  # only update if started and not finished!
            buttons = mouse_smart.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(smart, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_smart):
                            gotValidClick = True
                            mouse_smart.clicked_name.append(obj.name)
                    x, y = mouse_smart.getPos()
                    mouse_smart.x.append(x)
                    mouse_smart.y.append(y)
                    buttons = mouse_smart.getPressed()
                    mouse_smart.leftButton.append(buttons[0])
                    mouse_smart.midButton.append(buttons[1])
                    mouse_smart.rightButton.append(buttons[2])
                    mouse_smart.time.append(mouse_smart.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *text_trust* updates
        
        # if text_trust is starting this frame...
        if text_trust.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_trust.frameNStart = frameN  # exact frame index
            text_trust.tStart = t  # local t and not account for scr refresh
            text_trust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_trust, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_trust.started')
            # update status
            text_trust.status = STARTED
            text_trust.setAutoDraw(True)
        
        # if text_trust is active this frame...
        if text_trust.status == STARTED:
            # update params
            pass
        
        # *trust* updates
        
        # if trust is starting this frame...
        if trust.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            trust.frameNStart = frameN  # exact frame index
            trust.tStart = t  # local t and not account for scr refresh
            trust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trust, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trust.started')
            # update status
            trust.status = STARTED
            trust.setAutoDraw(True)
        
        # if trust is active this frame...
        if trust.status == STARTED:
            # update params
            pass
        # *mouse_trust* updates
        
        # if mouse_trust is starting this frame...
        if mouse_trust.status == NOT_STARTED and t >= 60-frameTolerance:
            # keep track of start time/frame for later
            mouse_trust.frameNStart = frameN  # exact frame index
            mouse_trust.tStart = t  # local t and not account for scr refresh
            mouse_trust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_trust, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_trust.started', t)
            # update status
            mouse_trust.status = STARTED
            mouse_trust.mouseClock.reset()
            prevButtonState = mouse_trust.getPressed()  # if button is down already this ISN'T a new click
        if mouse_trust.status == STARTED:  # only update if started and not finished!
            buttons = mouse_trust.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(trust, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_trust):
                            gotValidClick = True
                            mouse_trust.clicked_name.append(obj.name)
                    x, y = mouse_trust.getPos()
                    mouse_trust.x.append(x)
                    mouse_trust.y.append(y)
                    buttons = mouse_trust.getPressed()
                    mouse_trust.leftButton.append(buttons[0])
                    mouse_trust.midButton.append(buttons[1])
                    mouse_trust.rightButton.append(buttons[2])
                    mouse_trust.time.append(mouse_trust.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *key_resp_next* updates
        waitOnFlip = False
        
        # if key_resp_next is starting this frame...
        if key_resp_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_next.frameNStart = frameN  # exact frame index
            key_resp_next.tStart = t  # local t and not account for scr refresh
            key_resp_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_next.started')
            # update status
            key_resp_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_next.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_next.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_next_allKeys.extend(theseKeys)
            if len(_key_resp_next_allKeys):
                key_resp_next.keys = _key_resp_next_allKeys[-1].name  # just the last key pressed
                key_resp_next.rt = _key_resp_next_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
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
    trials_2.addData('believe.response', believe.getRating())
    trials_2.addData('believe.rt', believe.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse_believe.x', mouse_believe.x)
    trials_2.addData('mouse_believe.y', mouse_believe.y)
    trials_2.addData('mouse_believe.leftButton', mouse_believe.leftButton)
    trials_2.addData('mouse_believe.midButton', mouse_believe.midButton)
    trials_2.addData('mouse_believe.rightButton', mouse_believe.rightButton)
    trials_2.addData('mouse_believe.time', mouse_believe.time)
    trials_2.addData('mouse_believe.clicked_name', mouse_believe.clicked_name)
    trials_2.addData('nice.response', nice.getRating())
    trials_2.addData('nice.rt', nice.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse_nice.x', mouse_nice.x)
    trials_2.addData('mouse_nice.y', mouse_nice.y)
    trials_2.addData('mouse_nice.leftButton', mouse_nice.leftButton)
    trials_2.addData('mouse_nice.midButton', mouse_nice.midButton)
    trials_2.addData('mouse_nice.rightButton', mouse_nice.rightButton)
    trials_2.addData('mouse_nice.time', mouse_nice.time)
    trials_2.addData('mouse_nice.clicked_name', mouse_nice.clicked_name)
    trials_2.addData('smart.response', smart.getRating())
    trials_2.addData('smart.rt', smart.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse_smart.x', mouse_smart.x)
    trials_2.addData('mouse_smart.y', mouse_smart.y)
    trials_2.addData('mouse_smart.leftButton', mouse_smart.leftButton)
    trials_2.addData('mouse_smart.midButton', mouse_smart.midButton)
    trials_2.addData('mouse_smart.rightButton', mouse_smart.rightButton)
    trials_2.addData('mouse_smart.time', mouse_smart.time)
    trials_2.addData('mouse_smart.clicked_name', mouse_smart.clicked_name)
    trials_2.addData('trust.response', trust.getRating())
    trials_2.addData('trust.rt', trust.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse_trust.x', mouse_trust.x)
    trials_2.addData('mouse_trust.y', mouse_trust.y)
    trials_2.addData('mouse_trust.leftButton', mouse_trust.leftButton)
    trials_2.addData('mouse_trust.midButton', mouse_trust.midButton)
    trials_2.addData('mouse_trust.rightButton', mouse_trust.rightButton)
    trials_2.addData('mouse_trust.time', mouse_trust.time)
    trials_2.addData('mouse_trust.clicked_name', mouse_trust.clicked_name)
    # check responses
    if key_resp_next.keys in ['', [], None]:  # No response was made
        key_resp_next.keys = None
    trials_2.addData('key_resp_next.keys',key_resp_next.keys)
    if key_resp_next.keys != None:  # we had a response
        trials_2.addData('key_resp_next.rt', key_resp_next.rt)
    # the Routine "passages" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('samples.xlsx'),
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
    # update component parameters for each repeat
    sample_sounds.setSound('samples.xlsx', hamming=True)
    sample_sounds.setVolume(1.0, log=False)
    textbox_origin.reset()
    textbox_origin.setText('')
    textbox_firstlang.reset()
    textbox_firstlang.setText('')
    slider_recognize.reset()
    # reset end_button to account for continued clicks & clear times on/off
    end_button.reset()
    # keep track of which components have finished
    samplesComponents = [sample_sounds, textbox_origin, textbox_firstlang, recognize, slider_recognize, end_button]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sample_sounds is starting this frame...
        if sample_sounds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sample_sounds.frameNStart = frameN  # exact frame index
            sample_sounds.tStart = t  # local t and not account for scr refresh
            sample_sounds.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sample_sounds.started', tThisFlipGlobal)
            # update status
            sample_sounds.status = STARTED
            sample_sounds.play(when=win)  # sync with win flip
        # update sample_sounds status according to whether it's playing
        if sample_sounds.isPlaying:
            sample_sounds.status = STARTED
        elif sample_sounds.isFinished:
            sample_sounds.status = FINISHED
        
        # *textbox_origin* updates
        
        # if textbox_origin is starting this frame...
        if textbox_origin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_origin.frameNStart = frameN  # exact frame index
            textbox_origin.tStart = t  # local t and not account for scr refresh
            textbox_origin.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_origin, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_origin.started')
            # update status
            textbox_origin.status = STARTED
            textbox_origin.setAutoDraw(True)
        
        # if textbox_origin is active this frame...
        if textbox_origin.status == STARTED:
            # update params
            pass
        
        # *textbox_firstlang* updates
        
        # if textbox_firstlang is starting this frame...
        if textbox_firstlang.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_firstlang.frameNStart = frameN  # exact frame index
            textbox_firstlang.tStart = t  # local t and not account for scr refresh
            textbox_firstlang.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_firstlang, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_firstlang.started')
            # update status
            textbox_firstlang.status = STARTED
            textbox_firstlang.setAutoDraw(True)
        
        # if textbox_firstlang is active this frame...
        if textbox_firstlang.status == STARTED:
            # update params
            pass
        
        # *recognize* updates
        
        # if recognize is starting this frame...
        if recognize.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognize.frameNStart = frameN  # exact frame index
            recognize.tStart = t  # local t and not account for scr refresh
            recognize.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognize, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recognize.started')
            # update status
            recognize.status = STARTED
            recognize.setAutoDraw(True)
        
        # if recognize is active this frame...
        if recognize.status == STARTED:
            # update params
            pass
        
        # *slider_recognize* updates
        
        # if slider_recognize is starting this frame...
        if slider_recognize.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_recognize.frameNStart = frameN  # exact frame index
            slider_recognize.tStart = t  # local t and not account for scr refresh
            slider_recognize.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_recognize, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_recognize.started')
            # update status
            slider_recognize.status = STARTED
            slider_recognize.setAutoDraw(True)
        
        # if slider_recognize is active this frame...
        if slider_recognize.status == STARTED:
            # update params
            pass
        # *end_button* updates
        
        # if end_button is starting this frame...
        if end_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            end_button.frameNStart = frameN  # exact frame index
            end_button.tStart = t  # local t and not account for scr refresh
            end_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_button.started')
            # update status
            end_button.status = STARTED
            end_button.setAutoDraw(True)
        
        # if end_button is active this frame...
        if end_button.status == STARTED:
            # update params
            pass
            # check whether end_button has been pressed
            if end_button.isClicked:
                if not end_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    end_button.timesOn.append(end_button.buttonClock.getTime())
                    end_button.timesOff.append(end_button.buttonClock.getTime())
                elif len(end_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    end_button.timesOff[-1] = end_button.buttonClock.getTime()
                if not end_button.wasClicked:
                    # end routine when end_button is clicked
                    continueRoutine = False
                if not end_button.wasClicked:
                    # run callback code when end_button is clicked
                    pass
        # take note of whether end_button was clicked, so that next frame we know if clicks are new
        end_button.wasClicked = end_button.isClicked and end_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
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
    trials_3.addData('textbox_origin.text',textbox_origin.text)
    trials_3.addData('textbox_firstlang.text',textbox_firstlang.text)
    trials_3.addData('slider_recognize.response', slider_recognize.getRating())
    trials_3.addData('slider_recognize.rt', slider_recognize.getRT())
    trials_3.addData('end_button.numClicks', end_button.numClicks)
    if end_button.numClicks:
       trials_3.addData('end_button.timesOn', end_button.timesOn)
       trials_3.addData('end_button.timesOff', end_button.timesOff)
    else:
       trials_3.addData('end_button.timesOn', "")
       trials_3.addData('end_button.timesOff', "")
    # the Routine "samples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# --- Prepare to start Routine "thankyou" ---
continueRoutine = True
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
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    
    # if thank_you is starting this frame...
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you.started')
        # update status
        thank_you.status = STARTED
        thank_you.setAutoDraw(True)
    
    # if thank_you is active this frame...
    if thank_you.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
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
