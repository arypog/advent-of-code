main :: IO ()
main = do
    contents <- readFile "2025/00/pub"
    putStrLn contents