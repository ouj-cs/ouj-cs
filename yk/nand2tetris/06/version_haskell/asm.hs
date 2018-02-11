#!/usr/bin/env runhaskell
module Main (main) where

import qualified Data.Char
import qualified Numeric
import qualified System.Environment

linesWoComments :: [String] -> [String]
linesWoComments [] = []
linesWoComments (x:xs)
    | lineMod x == "" = linesWoComments xs
    | otherwise = lineMod x : linesWoComments xs
    where
    lineMod :: String -> String
    lineMod xs = trimR $ trimL $ noComment $ noNewline xs
        where
        noNewline :: String -> String
        noNewline [] = []
        noNewline ('\r':xs) = noNewline xs
        noNewline (x:xs) = x : noNewline xs
        noComment :: String -> String
        noComment [] = []
        noComment [x] = [x]
        noComment ('/':'/':xs) = ""
        noComment (x:xs) = x : noComment xs
        trimL :: String -> String
        trimL [] = []
        trimL (' ':xs) = trimL xs
        trimL xs = xs
        trimR :: String -> String
        trimR xs = reverse $ trimL $ reverse xs

mnemonics3 :: String -> [String]
mnemonics3 xs = [comp, dest, jump]
    where
    dest :: String
    dest = fst destNotdest
    comp :: String
    comp = tail $ fst compNotComp
    jump :: String
    jump = tail $ snd compNotComp
    destNotdest :: (String, String)
    destNotdest = break ('=' ==) s
    compAndJump :: String
    compAndJump = snd destNotdest
    compNotComp :: (String, String)
    compNotComp = break (';' ==) compAndJump
    s :: String
    s = addNull xs
        where
        addNull :: String -> String
        addNull xs = ensureRight $ ensureLeft xs
            where
            ensureLeft :: String -> String
            ensureLeft xs
                | hasEqual xs = xs
                | otherwise = "null=" ++ xs
                where
                hasEqual :: String -> Bool
                hasEqual [] = False
                hasEqual ('=':xs) = True
                hasEqual (x:xs) = hasEqual xs
            ensureRight :: String -> String
            ensureRight xs
                | hasSemicolon xs = xs
                | otherwise = xs ++ ";null"
                where
                hasSemicolon :: String -> Bool
                hasSemicolon [] = False
                hasSemicolon (';':xs) = True
                hasSemicolon (x:xs) = hasSemicolon xs

binComp :: String -> String
binComp = f
    where
    f "0" = "0101010"
    f "1" = "0111111"
    f "-1" = "0111010"
    f "D" = "0001100"
    f "A" = "0110000"
    f "!D" = "0001101"
    f "!A" = "0110001"
    f "-D" = "0001111"
    f "-A" = "0110011"
    f "D+1" = "0011111"
    f "A+1" = "0110111"
    f "D-1" = "0001110"
    f "A-1" = "0110010"
    f "D+A" = "0000010"
    f "D-A" = "0010011"
    f "A-D" = "0000111"
    f "D&A" = "0000000"
    f "D|A" = "0010101"
    f "M" = "1110000"
    f "!M" = "1110001"
    f "-M" = "1110011"
    f "M+1" = "1110111"
    f "M-1" = "1110010"
    f "D+M" = "1000010"
    f "D-M" = "1010011"
    f "M-D" = "1000111"
    f "D&M" = "1000000"
    f "D|M" = "1010101"

binDest :: String -> String
binDest = f
    where
    f "null" = "000"
    f "M" = "001"
    f "D" = "010"
    f "MD" = "011"
    f "A" = "100"
    f "AM" = "101"
    f "AD" = "110"
    f "AMD" = "111"

binJump :: String -> String
binJump = f
    where
    f "null" = "000"
    f "JGT" = "001"
    f "JEQ" = "010"
    f "JGE" = "011"
    f "JLT" = "100"
    f "JNE" = "101"
    f "JLE" = "110"
    f "JMP" = "111"

binFromAsm :: String -> String
binFromAsm s = unlines $ lines3 lines2
    where
    linesOrg :: [String]
    linesOrg = lines s
    lines2 :: [String]
    lines2 = linesWoComments linesOrg
    lines3 :: [String] -> [String]
    lines3 [] = []
    lines3 (x:xs)
        | isInstructionA x = binA x : lines3 xs
        | otherwise = binC x : lines3 xs
        where
        isInstructionA [] = False
        isInstructionA ('@':xs) = True
        isInstructionA _ = False
        binA instructionA = pad b
            where
            i :: Int
            i = read $ tail instructionA :: Int
            b :: String
            b = Numeric.showIntAtBase 2 Data.Char.intToDigit i ""
            pad :: String -> String
            pad xs
                | length xs < 16 = pad ('0':xs)
                | otherwise = xs
        binC instructionC = "111" ++ binaryComp ++ binaryDest ++ binaryJump
            where
            list = mnemonics3 instructionC
            mnemonicComp = head list
            mnemonicDest = list !! 1
            mnemonicJump = list !! 2
            binaryComp = binComp mnemonicComp
            binaryDest = binDest mnemonicDest
            binaryJump = binJump mnemonicJump

defaultTable :: [(String, Int)]
defaultTable = f 15 [] ++ [
    ("SP", 0), ("LCL", 1), ("ARG", 2), ("THIS", 3), ("THAT", 4),
    ("SCREEN", 16384), ("KBD", 245576)]
    where
    f i xs
        | i >= 0 = f (i - 1) (("R" ++ show i, i):xs)
        | otherwise = xs

asmWoLabels :: String -> String
asmWoLabels xs = unlines linesWoVars
    where
    linesOrg :: [String]
    linesOrg = linesWoComments $ lines xs
    doneLabels = woLabels linesOrg [] (reverse defaultTable) 0
        where
        woLabels :: [String] -> [String] -> [(String, Int)] -> Int -> ([String], [(String, Int)])
        woLabels [] ys zs _ = (reverse ys, reverse zs)
        woLabels (x:xs) ys zs i
            | isLabel x = woLabels xs ys ((label x, i):zs) i
            | otherwise = woLabels xs (x:ys) zs (i + 1)
            where
            isLabel [] = False
            isLabel ('(':xs) = True
            isLabel _ = False
            label xs = init $ tail xs
    linesWoLabels = fst doneLabels
    tableWoLabels = snd doneLabels
    doneVars = f linesWoLabels [] (reverse tableWoLabels) 16
        where
        f :: [String] -> [String] -> [(String, Int)] -> Int -> ([String], [(String, Int)])
        f [] ys zs _ = (reverse ys, reverse zs)
        f (x:xs) ys zs i
            | isNewVar x = f xs (("@" ++ show i):ys) (
            (tail x, i) : zs) (i + 1)
            | isVar x = f xs (("@" ++ show (value zs $ tail x)):ys) zs i
            | otherwise = f xs (x:ys) zs i
            where
            isVar x
                | isInstructionA x = (x !! 1) `notElem` "0123456789"
                | otherwise = False
                where
                isInstructionA = elem '@'
            isNewVar :: String -> Bool
            isNewVar x = isVar x && not (isDefined zs (tail x))
            isDefined [] _ = False
            isDefined (x:xs) key
                | fst x == key = True
                | otherwise = isDefined xs key
            value (x:xs) key
                | fst x == key = snd x
                | otherwise = value xs key
    linesWoVars = fst doneVars

main :: IO()
main = interact $ binFromAsm . asmWoLabels
