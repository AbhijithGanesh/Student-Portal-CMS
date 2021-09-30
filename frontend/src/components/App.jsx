import React from 'react';
import Typography from '@material-ui/core/typography'
import DenseAppBar from './header/header.jsx';

const HelloWorld = () => {
    return (
        <>
        <DenseAppBar/>
            <Typography variant = "h1">
                Hello World
            </Typography>
        </>
    )
}
export default HelloWorld;