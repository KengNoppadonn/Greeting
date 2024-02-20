import React from 'react';
import VideoPlayer from './VideoPlayer';

const App = () => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-8 offset-lg-2">
                    <VideoPlayer />
                </div>
            </div>
        </div>
    );
};

export default App;
