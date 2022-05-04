# TODO:
# Add clear button and replayability


import pygame
from sudoku import *
from time import sleep


class visualSudoku(Sudoku):
    def solve(self, i = 0, j = 0):
        if i == 9:
            return True
        if self.board[i][j] == '0':
            possible = self.check_row([i,j]).intersection(self.check_col([i,j]).intersection(self.check_box([i,j])))
            if possible == set():
                return False
            temp_board = []
            store_list(self.board, temp_board)
            for num in possible:
                copy_list(temp_board, self.board)
                self.place_number([i,j], str(num))
                
                draw(self.board, (i,j))
                #sleep(TIMER)

                if self.solve(i+(j+1)//9, (j+1)%9):
                    return True
            return False
        else:
            return self.solve(i+(j+1)//9, (j+1)%9)


def draw(board, position=None):
    display.fill((255, 255, 255))
    draw_board(board, position)
    draw_lines()
    draw_solve_box()
    pygame.display.update()


def draw_board(board, position):
    if position:
        row, col = position
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '0':
                num = ' '
            if position and [i, j] == [row, col]:
                text = font.render(num, True, (0, 0, 0), (0, 155, 15))
            else:
                text = font.render(num, True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = ((((j+1)*WIDTH//9)+(j*WIDTH//9))//2, (((i+1)*HEIGHT//9)+(i*HEIGHT//9))//2)
            display.blit(text, textRect)


def draw_lines():
    line_width = 2
    for i in range(9):
        if i % 3 == 0:
            pygame.draw.line(display, (0, 0, 0), (i*WIDTH//9, 0), (i*WIDTH//9, WIDTH), line_width+2)
        else:
            pygame.draw.line(display, (0, 0, 0), (i*WIDTH//9, 0), (i*WIDTH//9, WIDTH), line_width)
    pygame.draw.line(display, (0, 0, 0), (WIDTH-line_width, 0), (WIDTH-line_width, HEIGHT), line_width+2)
    for j in range(10):
        if j % 3 == 0:
            pygame.draw.line(display, (0, 0, 0), (0, j*HEIGHT//9), (HEIGHT, j*HEIGHT//9), line_width+2)
        else:
            pygame.draw.line(display, (0, 0, 0), (0, j*HEIGHT//9), (HEIGHT, j*HEIGHT//9), line_width)


def draw_solve_box():
    box = pygame.draw.rect(display, (0, 0, 0), (350, HEIGHT + 12, 200, 75), width = 2)
    text = font.render('Solve', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = box.center
    display.blit(text, textRect)


def find_box(x, y):
    return y//(HEIGHT//9), x//(WIDTH//9)


def run():
    selected_box = None
    stop = False
    # sudoku = visualSudoku('sample_boards/very_hard_board')
    sudoku = visualSudoku()
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if 350 <= x <= 550 and HEIGHT+12 <= y <= HEIGHT+87:
                    try:
                        sudoku.solve()
                        # print(sudoku)
                    except:
                        stop = True
                else:
                    selected_box = find_box(x, y)
            if event.type == pygame.KEYDOWN and selected_box:
                key = None
                if event.key == pygame.K_1:
                    key = '1'
                elif event.key == pygame.K_2:
                    key = '2'
                elif event.key == pygame.K_3:
                    key = '3'
                elif event.key == pygame.K_4:
                    key = '4' 
                elif event.key == pygame.K_5:
                    key = '5'
                elif event.key == pygame.K_6:
                    key = '6'
                elif event.key == pygame.K_7:
                    key = '7'
                elif event.key == pygame.K_8:
                    key = '8'
                elif event.key == pygame.K_9:
                    key = '9'
                elif event.key == pygame.K_0:
                    key = '0'
                if key:
                    sudoku.place_number(selected_box, key)
        draw(sudoku.board)
    pygame.quit()
        

if __name__ == '__main__':
    WIDTH, HEIGHT = 900, 900
    HEIGHT_OFFSET = 100
    RESOLUTION = (WIDTH, HEIGHT + HEIGHT_OFFSET)
    TIMER = 0.05

    pygame.init()
    display = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Sudoku')
    font = pygame.font.Font('freesansbold.ttf', 48)
    run()
