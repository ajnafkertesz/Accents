#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on Mon May 29 15:37:06 2023
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
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
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
expName = 'accent_Pt1'  # from the Builder filename that created this script
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
    originPath='/Users/ajnafannikertesz/Desktop/Accents /accent_Pt1.py',
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

# --- Initialize components for Routine "welcome" ---
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Welcome to the study!\n\nIn this study you will hear words that are either living or non-living things. For living things press "A" and for non-living things press "L". This is a study measuring response time, so try to be as fast as possible. If you make an error you can correct yourself and the button you pressed last will be recorded.\n\nPress SPACE to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_space = keyboard.Keyboard()

# --- Initialize components for Routine "words" ---
key_al = keyboard.Keyboard()
allwords = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='allwords')
allwords.setVolume(1.0)

# --- Initialize components for Routine "thankyou" ---
text_thanks = visual.TextStim(win=win, name='text_thanks',
    text='Thank you for your participation. Your responses have been recorded.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
# update component parameters for each repeat
key_space.keys = []
key_space.rt = []
_key_space_allKeys = []
# keep track of which components have finished
welcomeComponents = [text_welcome, key_space]
for thisComponent in welcomeComponents:
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

# --- Run Routine "welcome" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    
    # if text_welcome is starting this frame...
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_welcome.started')
        # update status
        text_welcome.status = STARTED
        text_welcome.setAutoDraw(True)
    
    # if text_welcome is active this frame...
    if text_welcome.status == STARTED:
        # update params
        pass
    
    # *key_space* updates
    waitOnFlip = False
    
    # if key_space is starting this frame...
    if key_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_space.frameNStart = frameN  # exact frame index
        key_space.tStart = t  # local t and not account for scr refresh
        key_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_space, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_space.started')
        # update status
        key_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_space.status == STARTED and not waitOnFlip:
        theseKeys = key_space.getKeys(keyList=['space'], waitRelease=False)
        _key_space_allKeys.extend(theseKeys)
        if len(_key_space_allKeys):
            key_space.keys = _key_space_allKeys[-1].name  # just the last key pressed
            key_space.rt = _key_space_allKeys[-1].rt
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
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_space.keys in ['', [], None]:  # No response was made
    key_space.keys = None
thisExp.addData('key_space.keys',key_space.keys)
if key_space.keys != None:  # we had a response
    thisExp.addData('key_space.rt', key_space.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
word_rep = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='word_rep')
thisExp.addLoop(word_rep)  # add the loop to the experiment
thisWord_rep = word_rep.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWord_rep.rgb)
if thisWord_rep != None:
    for paramName in thisWord_rep:
        exec('{} = thisWord_rep[paramName]'.format(paramName))

for thisWord_rep in word_rep:
    currentLoop = word_rep
    # abbreviate parameter names if possible (e.g. rgb = thisWord_rep.rgb)
    if thisWord_rep != None:
        for paramName in thisWord_rep:
            exec('{} = thisWord_rep[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "words" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_al.keys = []
    key_al.rt = []
    _key_al_allKeys = []
    allwords.setSound('words.xlsx', hamming=True)
    allwords.setVolume(1.0, log=False)
    # keep track of which components have finished
    wordsComponents = [key_al, allwords]
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
        
        # *key_al* updates
        waitOnFlip = False
        
        # if key_al is starting this frame...
        if key_al.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_al.frameNStart = frameN  # exact frame index
            key_al.tStart = t  # local t and not account for scr refresh
            key_al.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_al, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_al.started')
            # update status
            key_al.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_al.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_al.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_al.status == STARTED and not waitOnFlip:
            theseKeys = key_al.getKeys(keyList=['a','l'], waitRelease=False)
            _key_al_allKeys.extend(theseKeys)
            if len(_key_al_allKeys):
                key_al.keys = _key_al_allKeys[-1].name  # just the last key pressed
                key_al.rt = _key_al_allKeys[-1].rt
        
        # if allwords is starting this frame...
        if allwords.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            allwords.frameNStart = frameN  # exact frame index
            allwords.tStart = t  # local t and not account for scr refresh
            allwords.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('allwords.started', tThisFlipGlobal)
            # update status
            allwords.status = STARTED
            allwords.play(when=win)  # sync with win flip
        # update allwords status according to whether it's playing
        if allwords.isPlaying:
            allwords.status = STARTED
        elif allwords.isFinished:
            allwords.status = FINISHED
        
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
    if key_al.keys in ['', [], None]:  # No response was made
        key_al.keys = None
    word_rep.addData('key_al.keys',key_al.keys)
    if key_al.keys != None:  # we had a response
        word_rep.addData('key_al.rt', key_al.rt)
    allwords.stop()  # ensure sound has stopped at end of routine
    # the Routine "words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'word_rep'


# --- Prepare to start Routine "thankyou" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
thankyouComponents = [text_thanks]
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
    
    # *text_thanks* updates
    
    # if text_thanks is starting this frame...
    if text_thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_thanks.frameNStart = frameN  # exact frame index
        text_thanks.tStart = t  # local t and not account for scr refresh
        text_thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_thanks, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_thanks.started')
        # update status
        text_thanks.status = STARTED
        text_thanks.setAutoDraw(True)
    
    # if text_thanks is active this frame...
    if text_thanks.status == STARTED:
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
