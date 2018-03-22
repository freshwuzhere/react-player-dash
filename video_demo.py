import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import ipop_components as ipop

import react_player_dash as rpd

app = dash.Dash()

app.scripts.config.serve_locally = True  # note script is searched for in unpkg.com if this is not set.

app.layout = html.Div(children=[
     html.H1(children='REACT-PLAYER-DASH DEMO'
            ),

html.Div(id = 'time_counter',
         children='''NO TIME YET'''),

html.Div(id = 'playback_speed',
         children='''no speed yet'''),

html.Div(id = 'duration_return',
         children='''not duration yet'''),

html.Div(id = 'playback_volume',
         children='''set at default volume'''),

html.Div(id = 'muted',
         children='''default mute'''),

html.Div(children=[
    # html.Button('', id='play_button', className='fa fa-play'),
    ipop.Button('', id='play_button', className='fa fa-play'),
    ipop.Button('', id='stop_button', className='fa fa-stop'),
    ipop.Button('Quiet', id='quiet_button', className='button'),
    ipop.Button('Middle Vol', id='mid_vol_button', className='button'),
    ipop.Button('LOUD!', id='LOUD_button', className='button'),
    ipop.Button('', id='unmute_button', className='fa fa-volume-up'),
    ipop.Button('', id='mute_button', className='fa fa-volume-off'),

]
),

    html.Div(children=[
    ipop.Button('Half Speed', id='half_speed_button', className='button'),
    ipop.Button('Regular Speed', id='normal_speed_button', className='button'),
    ipop.Button('Double Speed', id='double_speed_button', className='button'),
    ipop.Button('Seek 10s', id='seek_10_button', className='button'),
    ipop.Button('Seek middle', id='seek_middle_button', className='button'),
    ipop.Button('Seek 100s', id='seek_100_button', className='button'),
    ]
),

#  THIS IS HTML VIDEO - addappted to my own
rpd.my_Player(
    id = 'video_player',
    url = "https://www.youtube.com/watch?v=ysz5S6PUM-U",
    # url = 'http://127.0.0.1:8000/video_5.mp4',
    width = 900,
    height = 720,
    controls = True,
    cursorUpdate = 5000,
    playing = True ),


# dcc.Interval(    # this firsts a trigger every 5 seconds
#     id='interval-component',
#     interval=1 * 5000,  # in milliseconds
#     n_intervals=0
#     ),
    ]
)

@app.callback(
    dash.dependencies.Output('playback_speed', 'children'),
    [dash.dependencies.Input('video_player', 'playbackRate')])
def update_playback(n):
    return("Playback Speed -  {:.2f}".format(n))


### Receives current cursor time from video component on regular intervals - set when called.
@app.callback(
    dash.dependencies.Output('time_counter', 'children'),
    [dash.dependencies.Input('video_player', 'currTime')])
def update_timer(currentTime):
    return("Time - {}".format(currentTime))

### Receives the video duration which is collected using the 'onReady' command of reac-player
@app.callback(
    dash.dependencies.Output('duration_return', 'children'),
    [dash.dependencies.Input('video_player', 'duration')])
def update_duration(duration):
    return("Duration - {}".format(str(duration)))

@app.callback(
    dash.dependencies.Output('playback_volume', 'children'),
    [dash.dependencies.Input('video_player', 'volume')])
def update_playback(n):
    return("Volume -  {:.2f}".format(n))

@app.callback(
    dash.dependencies.Output('muted', 'children'),
    [dash.dependencies.Input('video_player', 'muted')])
def update_playback(n):
    return("Muted -" + str(n))


@app.callback(Output('video_player','playing'),
              [Input('play_button','n_clicks'),
               Input('stop_button', 'n_clicks'),
               ],
              [State('play_button','n_clicks_previous'),
               State('stop_button', 'n_clicks_previous'),
              ],
              )
def update_player(play_NOC, stop_NOC,play_NOCP, stop_NOCP):
    ### accept play or stop button pushes - act accordingly
    if play_NOC != play_NOCP:
        #  somebody pressed the play button
        return( True)
    elif stop_NOC != stop_NOCP:
        # somebody pressed the STOP button
        return(False)
    else:
        # this is the initial run through and should stop the player
        return(False)

@app.callback(Output('video_player','playbackRate'),
              [ Input('half_speed_button','n_clicks'),
                Input('normal_speed_button', 'n_clicks'),
                Input('double_speed_button', 'n_clicks'),
               ],
              [ State('half_speed_button','n_clicks_previous'),
                State('normal_speed_button', 'n_clicks_previous'),
                State('double_speed_button', 'n_clicks_previous'),
              ],
              )
def update_player_speed(half_NOC, normal_NOC, double_NOC, half_NOCP, normal_NOCP, double_NOCP):
    # This recieves the button clicks and acts accordingly
    if half_NOC != half_NOCP:
        #  somebody pressed the play button
        return(0.5)
    elif normal_NOC != normal_NOCP:
        # somebody pressed the STOP button
        return(1.0)
    elif double_NOC != double_NOCP:
        # somebody pressed the STOP button
        return(2.0)
    else:
        # this is the initial run through and shoudl stop the player
        return(1.0)

@app.callback(Output('video_player','volume'),
              [ Input('quiet_button','n_clicks'),
                Input('mid_vol_button', 'n_clicks'),
                Input('LOUD_button', 'n_clicks'),
               ],
              [ State('quiet_button','n_clicks_previous'),
                State('mid_vol_button', 'n_clicks_previous'),
                State('LOUD_button', 'n_clicks_previous'),
              ],
              )
def update_player_volume(half_NOC, normal_NOC, double_NOC, half_NOCP, normal_NOCP, double_NOCP):
    # This recieves the button clicks and acts accordingly
    if half_NOC != half_NOCP:
        #  somebody pressed the play button
        return(0.1)
    elif normal_NOC != normal_NOCP:
        # somebody pressed the STOP button
        return(0.5)
    elif double_NOC != double_NOCP:
        # somebody pressed the STOP button
        return(1.0)
    else:
        # this is the initial run through and shoudl stop the player
        return()

@app.callback(Output('video_player','muted'),
              [Input('unmute_button','n_clicks'),
               Input('mute_button', 'n_clicks'),
               ],
              [State('unmute_button','n_clicks_previous'),
               State('mute_button', 'n_clicks_previous'),
              ],
              )
def update_player(play_NOC, stop_NOC,play_NOCP, stop_NOCP):
    ### accept play or stop button pushes - act accordingly
    if play_NOC != play_NOCP:
        #  somebody pressed the play button
        return(False)
    elif stop_NOC != stop_NOCP:
        # somebody pressed the STOP button
        return(True)
    else:
        # this is the initial run through and should stop the player
        return(False)

@app.callback(Output('video_player','seekTo'),
              [ Input('seek_10_button','n_clicks'),
                Input('seek_middle_button', 'n_clicks'),
                Input('seek_100_button', 'n_clicks'),
               ],
              [ State('seek_10_button','n_clicks_previous'),
                State('seek_middle_button', 'n_clicks_previous'),
                State('seek_100_button', 'n_clicks_previous'),
                State('duration_return', 'children'),
              ],
              )
def update_player_seek(seek_10_NOC, seek_mid_NOC, seek_100_NOC, seek_10_NOCP, seek_mid_NOCP, seek_100_NOCP , duration_string):
    # This recieves the button clicks and acts accordingly
    if seek_10_NOC != seek_10_NOCP:
        #  somebody pressed the play button
        return(10.0)
    elif seek_mid_NOC != seek_mid_NOCP:
        # somebody pressed the STOP button
        duration = float(duration_string[11:])
        return(duration/2.0)
    elif seek_100_NOC != seek_100_NOCP:
        # somebody pressed the STOP button
        return(100.0)
    else:
        # this is the initial run through and shoudl stop the player
        # return(300.0)
        return(0)

# @app.callback(Output('video_player','seekTo'),
#               [ Input('seek_10_button','n_clicks'),])
# def test_seek(n_clicks):
#     return(10.0)



# TESTING
#  Tested
#   Playing (True or False)
#   Volume (between 0 and 1)
#   seekTo
#   muted
#   playbackRate
#   getCurrentTime
#   getDuration
#  To BE Tested
#   controls (volume only)
#   styles
#   playsInline
#   config


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.css.append_css({
    'external_url': 'https://unpkg.com/video-react@0.9.4/dist/video-react.css'})

app.css.append_css({
    'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'})

if __name__ == '__main__':
    app.run_server(debug=True)






# // Can be used to trigger functions using properties but beware - changing props fires infinite loop if done here
# // case
# 'targetSeekTo': {                // Works but is too jumpy with the call back - determined to do it externally with 1 sec timer feedback.
# // console.log('in targetSeek val = ' + String(newProps['targetSeekTo']));
# // // first get the current play position in time
# // const max_lag = 2
# // const max_accel = 0.1
# // const currTime_now = this.refs.player.getCurrentTime();
# // const targetTime = newProps['targetSeekTo'];
# // const delta_secs = targetTime - currTime_now;
# // console.log('delta secs = ' + String(delta_secs));
# // if (Math.abs(delta_secs) > max_lag) {
# // console.log('direct seek = ' + String(newProps['targetSeekTo']));
# // this.refs.player.seekTo(targetTime);
# //}
# // else {
# // const lag_factor = delta_secs / max_lag;
# // const pb_rate = this.refs.player.props.playbackRate;
# // var target_pb_rate = 1;
# // target_pb_rate = pb_rate + (pb_rate * lag_factor * max_accel ); // added dampener term 0.9
# // console.log('at calc 1 = ' + String(target_pb_rate) + 'pb_rate' + pb_rate + 'lag_factor ' + String(lag_factor));
# // if (Math.abs(target_pb_rate - pb_rate) > 0.05) {
# // newProps['playbackRate'] = target_pb_rate;
# // console.log('Making change')
# //}
# //}
# // // console.log('leaving targetSeek');
# //
# break;
# //}
