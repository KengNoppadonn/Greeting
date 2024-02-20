import React, { useEffect, useRef } from 'react';

const VideoPlayer = () => {
    const videoRef = useRef();

    useEffect(() => {
        const videoElement = videoRef.current;

        const loadVideo = () => {
            videoElement.src = '/video_feed';
            videoElement.load();
            videoElement.play();
        };

        loadVideo();

        return () => {
            videoElement.src = '';
        };
    }, []);

    return (
        <div>
            <h3 className="mt-5">Live Streaming kios</h3>
            <video ref={videoRef} width="100%" controls />
        </div>
    );
};

export default VideoPlayer;
