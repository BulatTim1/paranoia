import React from 'react';
import './AdaptiveVideoBox.css';

// @ts-ignore
const AdaptiveVideoBox = ({videoSrc}) => {
    const [setWidth] = React.useState(0);
    const [setHeight] = React.useState(0);

    const handleResize = () => {
        const videoContainer = document.getElementById('video-container');
        // @ts-ignore
        const videoWidth = videoContainer.offsetWidth;
        const videoHeight = videoWidth; // set height to match width for 1:1 aspect ratio

        // @ts-ignore
        setWidth(videoWidth);
        // @ts-ignore
        setHeight(videoHeight);
    };

    React.useEffect(() => {
        handleResize();
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    const videoStyles = {
        width: '100%',
        height: '100%',
        objectFit: 'cover',
    };

    const containerStyles = {
        position: 'relative',
        width: '100%',
        height: 0,
        paddingBottom: '100%', // 1:1 aspect ratio
    };

    return (
        // @ts-ignore
        <div id="video-container" style={containerStyles}>
            {/* @ts-ignore */}
            <video src={videoSrc} style={videoStyles} controls/>
        </div>
    );
};

export default AdaptiveVideoBox;