import React, { useEffect } from 'react'
import { Stack, Button } from '@chakra-ui/react'
import { useAuth0 } from "@auth0/auth0-react";
import { useNavigate } from 'react-router-dom'


interface LoginButtonProps {
  mr?: number
}

export const LoginButton = ({mr}: LoginButtonProps) => {
  const { loginWithRedirect, isAuthenticated, isLoading } = useAuth0()
  let navigate = useNavigate()

  useEffect(() => {
    isAuthenticated && navigate('/main')
  }, [navigate, isAuthenticated])

  return (
    <Stack direction='column' spacing={4} align='center'>
        <p style={{fontWeight: 'bold', fontSize: '24px'}}>RULES:</p>
        <p>Ant (default) - Moves 1 up, takes diagonally</p>
        <p>Squirrel (Tier 1) - Moves 2 up on its first move. Moves up 1 for each additional move, takes diagonally.</p>
        <p>Swan (Tier 2) - Can jump 2 on its first move. Can move up or diagonally up 1 for each additional move, takes up and diagonally.</p>
        <p>Turtle (Tier 2) - KING - Can move 1 and take in any direction.</p>
        <p>Monkey (Tier 1) - KING - Can move 1 and take in any direction. Can also switch places with friendly pieces.</p>
        <p>pon (Tier 2) - KING - Can move 2 and take in any 1 direction</p>
        <p>Bee (default) - Can move up, down, left, and right in any direction. Dies when it takes.</p>
        <p>Fox (Tier 1) - Can move up, down, left, and right as far as possible until contact.</p>
        <p>Tiger (Tier 2) - Can move as far as possible until contact in any direction.</p>
        <Button
          isLoading={isLoading}
          loadingText='Loading'
          colorScheme='black'
          variant='outline'
          spinnerPlacement='start'
          onClick={loginWithRedirect}
          mr={mr}
        >
          Log In 
        </Button> 
    </Stack>
  ) 
}