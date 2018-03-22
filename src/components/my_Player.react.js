import React, { Component, PropTypes } from 'react';
import ReactPlayer from 'react-player';

// Version 1.0.9

export default class my_Player extends Component {
  constructor(props, context) {
    super(props, context);
    this.myTimer = this.myTimer.bind(this);
    if (props.cursorUpdate === undefined){  // when user does not define - defaults to 1000 msec
        props.cursorUpdate = 1000
        const {setProps} = props;  // need to update props so it is defined
        if (setProps !== null) {
            setProps({cursorUpdate: 1000});
        }
    }
    this.myVar = setInterval(this.myTimer, props.cursorUpdate);  // this timer varies how often the timer feedback is updated.
    // console.log('cursorUpdate = ' + String(props.cursorUpdate))
  }

    //********
   propsToFunctions(oldProps, newProps ) {
         for(var prop in newProps) {
            // console.log(' prop = '+ String(prop) + ' old prop val = ' + String(oldProps[prop]) + String(prop) + ' new prop val = ' + String(newProps[prop]) );
            if (newProps[prop] != undefined){
                switch (prop) {
                     case 'seekTo': {
                         if (oldProps['seekTo'] !== newProps['seekTo']) {
                             this.refs.player.seekTo(newProps['seekTo']);
                             // console.log(' SeekTo  = ' + newProps['seekTo'])
                         }
                        break;
                    }
                    default:
                        // console.log(' default hit ');
                }
            }
        }
   }

    componentWillReceiveProps( newProps) {
        // take some action for functions that need to fire from our DASH props input
        // first get teh current props to compare to - only change the ones we need
        const oldProps = this.props;
        this.propsToFunctions(oldProps, newProps )
    }
    
    myTimer() {
        // actions when timer fires - the call to duration is a little redundant so regularly
        this.getCurrentTime()
    }

    getCurrentTime() {
        // THis function retrieves the current time and places in currTime property to be retrieved by DASH
        const {setProps} = this.props;
        const currTime_now = this.refs.player.getCurrentTime();
        if (setProps !== null) {
            setProps({currTime: currTime_now});
        }
    }

    getCurrentDuration() {
        const {setProps} = this.props;
        const duration_now = this.refs.player.getDuration();
        if (setProps !== null) {
          setProps({duration: duration_now});
        }
    }


  render() {
      const{
          url,
          width,
          height,
          playing,
          playsInline,
          playbackRate,
          muted,
          volume,
          cursorUpdate
      } = this.props;

    return (
      <div>
        <ReactPlayer
          ref="player"

          getCurrentTime={this.getCurrentTime}
          width={width}
          height={height}
          url={url}
          playing={playing}
          playsInline={playsInline}
          playbackRate={playbackRate}
          muted={muted}
          volume={volume}
          cursorUpdate= {cursorUpdate}
          onReady={() => this.getCurrentDuration()}
          controls = {true}
        >
        </ReactPlayer>
      </div>

    );
  }
}

my_Player.propTypes = {

	id: PropTypes.string,

    /**
     * width of video player
     */
      width: PropTypes.number,

    /**
     * height of video player
     */
      height: PropTypes.number,

    /**
     * src of video
     */
      url: PropTypes.string,

    /**
     * set true of false to start stop playing
     */
     playing: PropTypes.bool,


    /**
     * inline player
     */
      playsInline: PropTypes.bool,

   /**
     * cursor update rate in mSec
     */
      cursorUpdate: PropTypes.number,


       /**
     * SHow Controls?
     */
      controls: PropTypes.bool,


     /**
     * set playback rate - useful! multiple of normal = 1
     */
      playbackRate: PropTypes.number,

    /**
     * muted or not
     */
      muted: PropTypes.bool,

    /**
     * preset volume set number
     */
      volume: PropTypes.number,

    /**
     * seek time of video seconds
     */
      seekTo: PropTypes.number,

    /**
     * Target seek time of video seconds - uses function to speed up/slowdown or skip to location
     */
      targetSeekTo: PropTypes.number,

    /**
     *  curentTime from video
     */
      currTime: PropTypes.number,

    /**
     *  duration of video
     */
      duration: PropTypes.number,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * Dash-assigned callback that gets fired when the value changes.
     */
    // dashEvents: PropTypes.oneOf(['click','change'])
    dashEvents: PropTypes.oneOf(['change'])


};


