import React from 'react'
import { LogoutButton } from './LogoutButton'
import { Flex, Spacer } from '@chakra-ui/react'
import { useAuth0 } from '@auth0/auth0-react'

interface NavProps {
    text?: string
}

export const Nav = ({text: NavProps}: NavProps): JSX.Element => {
    const { isAuthenticated, user } = useAuth0()

    return (
        <Flex as='header' w='100vw' h='50px' position='fixed'>
            <LogoutButton ml='2'/>
            <Spacer />
            <p style={{margin: '8px', fontWeight: 'bold'}}> {user?.nickname}</p>
        </Flex>
    )
}