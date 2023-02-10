import styled from "styled-components";

export const Header = styled.div `
    position: relative;
    width: 95vw;
    height: 60px;
    float: left;
`

export const MenuItem = styled.button `
    @keyframes changeText {
        from {font-size: 1.0rem;}
        to {font-size: 1.2rem;}
    }
    width: 120px;
    height: 60px;
    background-color: #fff;
    border: none;
    float: right;
    font-size: 1.0rem;
    margin-right: 20px;
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    text-align: center;
`

export const Page = styled.div `
    width: 100vw;
    height: 100vh;
    background-color: #fff;
`

export const Logo = styled.img `
    width: 120px;
    height: auto;
    float: left;
    padding: 20px;
    padding-left: 40px;
`
export const Line = styled.div `
    padding-top: 60px;
    width: 100vw;
    display: flex;
    justify-content: center !important;
`