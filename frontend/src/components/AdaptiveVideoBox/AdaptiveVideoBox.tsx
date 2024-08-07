import React, { useState, useEffect } from 'react';

interface AdaptiveVideoBoxProps {
    videoSrc: string;
}

const AdaptiveVideoBox: React.FC<AdaptiveVideoBoxProps> = ({ videoSrc }) => {
    const [width, setWidth] = useState(0);
    const [height, setHeight] = useState(0);

    const handleResize = () => {
        const videoContainer = document.getElementById('video-container');
        const videoWidth = videoContainer.offsetWidth;
        const videoHeight = videoWidth; // set height to match width for 1:1 aspect ratio

        setWidth(videoWidth);
        setHeight(videoHeight);
    };

    useEffect(() => {
        handleResize();
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    const videoStyles: React.CSSProperties = {
        width: '100%',
        height: '100%',
        objectFit: 'cover',
    };

    const containerStyles: React.CSSProperties = {
        position: 'relative',
        width: '100%',
        height: 0,
        paddingBottom: '100%', // 1:1 aspect ratio
    };

    return (
        <div id="video-container" style={containerStyles}>
            <video src={videoSrc} style={videoStyles} />
        </div>
    );
};

export default AdaptiveVideoBox;