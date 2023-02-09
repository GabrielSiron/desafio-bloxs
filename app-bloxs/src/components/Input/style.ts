import styled from "styled-components";
type ProtoType = {
    validation: any;
};
const CommonInput = styled.input`
    padding: 10px;
    font-size: 1.0rem;
    box-sizing: border-box;
    border-radius: 8px;
    font-family: 'inter-regular'; 
    outline: 0;
`;


export const InputPasswordContainer = styled.div`
    width: 100%;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 8px;
    background-color: rgba(0, 0, 0, .0);
    border: 2px solid #6A6A6A;
    box-sizing: border-box;
    margin-top: 10px;
    padding-right: 10px;
`

export const InputPassword = styled(CommonInput)`
    width: 100%;
    height: 100%;
    border: none;
`;

export const PasswordPreview = styled.button`
    min-width: 25px;
    min-height: 20px;
    background-color: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    border: none;
    cursor: pointer;
`
export const IncorrectEmailWarning = styled.p`
    align-self: flex-start;
    font-family:'inter-regular';
    color: #eb4d4b;
    margin-top: 10px;
`
export const Input = styled(CommonInput).attrs((props:ProtoType)=>({
    border: props.validation,
}))<ProtoType>`
    width: 100%;
    height: 50px;
    background-color: rgba(0, 0, 0, .0);
    border: 2px solid ${(props)=>props.validation == null ? '#6A6A6A' : props.validation == false ? '#eb4d4b' : props.validation == true ? '#2ecc71' : ''};
    margin-top: 10px;
`;