import styled from "styled-components"; 
import { ActionButton } from "../home/style";

export const Text = styled.h2 `
    font-family: 'poppins';
    font-size: 1.2rem;
    padding: 12px;
    text-align: center;
`

export const TextContainer = styled.div `
    padding-top: 30px;
    display: flex;
    flex-direction: column;
`

export const ChangeAccountStatus = styled(ActionButton) `
    width: 200px;
    height: 60px;
    margin: 10px calc(50% - 100px);
`