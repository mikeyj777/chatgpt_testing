#include <SDL.h>

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

// Function prototypes
void drawBall(SDL_Renderer* renderer, int x, int y);

int main(int argc, char* argv[]) {
  // Initialize SDL
  if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    SDL_LogError(SDL_LOG_CATEGORY_ERROR, "Could not initialize SDL: %s", SDL_GetError());
    return 1;
  }

  // Create the window and renderer
  SDL_Window* window = SDL_CreateWindow("Bouncing Ball", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                                        SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
  SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

  // Initialize the ball position and velocity
  int x = SCREEN_WIDTH / 2;
  int y = SCREEN_HEIGHT / 2;
  int dx = 1;
  int dy = 1;

  // Main loop
  bool running = true;
  while (running) {
    // Handle events
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
      if (event.type == SDL_QUIT) {
        running = false;
      }
    }

    // Update the ball position
    x += dx;
    y += dy;

    // Check for collision with the walls
    if (x < 0 || x > SCREEN_WIDTH) {
      dx = -dx;
    }
    if (y < 0 || y > SCREEN_HEIGHT) {
      dy = -dy;
    }

    // Clear the screen
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    // Draw the ball
    drawBall(renderer, x, y);

    // Update the screen
    SDL_RenderPresent(renderer);
  }

  // Clean up
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();

  return 0;
}

// Function to draw a ball on the screen
void drawBall(SDL_Renderer* renderer, int x, int y) {
  SDL_Rect rect = { x - 10, y - 10, 20, 20 };
  SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
  SDL_RenderFillRect(renderer, &rect);
}
