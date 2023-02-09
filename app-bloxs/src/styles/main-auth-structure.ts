import styled from "styled-components";

export const AuthPage = styled.div`
    width: 100%;
    height: 100vh;
`;

export const MainView = styled.div`
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: absolute;
    z-index: 10;
    backdrop-filter: blur(10px);
    background-color: rgba(27, 31, 69, .56);
    box-sizing: border-box;
    padding: 90px 20px 20px 20px;
`;

export const GoToLogin = styled.button `
        width: 100%;
    height: 50px;
    border-radius: 8px;
    font-family: 'inter-medium';
    font-size: 1.2rem;
    color: #80b7ff;
    background-color: transparent;
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    border: none;
    transition: .2s ease-out;
    margin-top: 10px;
`

export const MainTitle = styled.h1`
    max-width: 593px;
    font-size: 3.5rem;
    text-align: center;
    color: #fff;
    font-family: 'inter-bold';
`;

export const SubTitle = styled.h2`
    font-size: 1.3rem;
    color: #fff;
    font-family: 'inter-regular';
    margin-top: 20px;
`

export const ImageContainer = styled.div`
    position: absolute;
    z-index: 5;
    width: 100%;
    height: 100%;
    overflow: hidden;
`;

export const PoweredContainer = styled.div`
    display: flex;
    align-items: center;
    position: absolute;
    bottom: 20px;
`;

export const PoweredTxt = styled.h3`
    color: #fff;
    font-size: 1.3rem;
    margin-right: 10px;
    font-family: 'inter-semibold';
`;

export const AuthSide = styled.section`
    display: flex;
    flex-direction: column;
    align-items: center;
    box-sizing: border-box;
    padding: 10px 0;
    justify-content: center;
`;

export const WelcomeContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
`;

export const AuthTitle = styled.h4`
    font-size: 5rem;
    color: #171D51;
    font-family: 'inter-bold';
`;

export const AuthSubTitle = styled.h5`
    font-size: 1.5rem;
    color: #171D51;
    font-family: 'inter-light';
    margin-top: 10px;
`;
export const Form = styled.form`
    width: 300px;
    /* background-color: green; */
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
`;

export const ActionButton = styled.button`
    width: 100%;
    height: 50px;
    border-radius: 8px;
    font-family: 'inter-medium';
    font-size: 1.2rem;
    color: #fff;
    background-color: ${props=>props.disabled ? '#AAD0FF' : '#57A0FF'};
    cursor: ${props=>props.disabled ? 'default' : 'pointer'};
    border: none;
    transition: .2s ease-out;
    margin-top: 40px;
    &:hover{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#80b7ff'};
    }
    &:active{
        background-color: ${props=>props.disabled ? '#AAD0FF' : '#377ad2'};
    }

`;