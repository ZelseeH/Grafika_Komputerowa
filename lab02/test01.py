import pygame
import math

# Inicjalizacja pygame
pygame.init()

# Ustawienia okna
window_size = (600, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dziesięciokąt Foremny")

# Kolory
background_color = (255, 255, 0)  # Żółty background
polygon_color = (245, 245, 220)  # Kremowy kolor dziesięciokąta
border_color = (0, 0, 0)  # Kolor obramówki
center_color = (200, 200, 180)  # Ciemniejszy kolor w środku dziesięciokąta

# Promień dziesięciokąta
radius = 150

# Środek okna
center_x, center_y = window_size[0] // 2, window_size[1] // 2

# Inicjalizacja wzoru
reference_vertices = [(center_x + int(radius * math.cos(2 * math.pi * i / 10)),
                       center_y + int(radius * math.sin(2 * math.pi * i / 10)))
                      for i in range(10)]

# Kopia wzoru, na której będą dokonywane przekształcenia
vertices = reference_vertices.copy()

# Główna pętla programu
running = True
display_polygon = True  # Zmienna do kontrolowania wyświetlania dziesięciokąta

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # Wyświetlanie dziesięciokąta dla klawisza 1
                vertices = reference_vertices.copy()
                display_polygon = True
            elif event.key == pygame.K_2:
                # Powiększenie i obrócenie dziesięciokąta o 45 stopni dla klawisza 2
                vertices = [(2 * x - center_x, 2 * y - center_y) for x, y in reference_vertices]
                angle = math.radians(45)
                vertices = [(int((x - center_x) * math.cos(angle) - (y - center_y) * math.sin(angle) + center_x),
                             int((x - center_x) * math.sin(angle) + (y - center_y) * math.cos(angle) + center_y))
                            for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_3:
                # Odwrócenie dziesięciokąta do góry nogami i rozciągnięcie dwukrotnie w pionie dla klawisza 3
                vertices = [(x, 2 * center_y - y) for x, y in reference_vertices]
                vertices = [(x, int(2 * (y - center_y) + center_y)) for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_4:
                # Efekt "shear" dla klawisza 4
                shear_factor = 0.4
                vertices = [(x + shear_factor * y, y) for x, y in reference_vertices]
                
                # Wycentrowanie "ściętego" dziesięciokąta
                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - center_x
                vertices = [(x - shift_x, y) for x, y in vertices]
                
                display_polygon = True
            elif event.key == pygame.K_5:
                   # Efekt dla klawisza 5
                scale_factor_x = 2
                scale_factor_y = 1
                translation_y = -158
                
                # Skalowanie
                vertices = [(scale_factor_x * x, scale_factor_y * y) for x, y in reference_vertices]
                
                # Translacja w pionie
                vertices = [(x, y + translation_y) for x, y in vertices]
                
                # Obliczenie przesunięcia w poziomie, aby utrzymać dziesięciokąt na środku
                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - center_x
                vertices = [(x - shift_x, y) for x, y in vertices]
                
                display_polygon = True
            elif event.key == pygame.K_6:
                        # Efekt dla klawisza 6
                shear_factor_y = -0.4
                angle_rotation = 0 # Obrót w prawo o 90 stopni
                
                # Shear w pionie
                vertices = [(x, x * shear_factor_y + y) for x, y in reference_vertices]
                
                # Obrót
                angle_rad = math.radians(angle_rotation)
                vertices = [(int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                            int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                            for x, y in vertices]
                            # Obliczenie przesunięcia w poziomie, aby utrzymać dziesięciokąt na środku
                min_y = min(vertices, key=lambda point: point[1])[1]
                max_y = max(vertices, key=lambda point: point[1])[1]
                shift_y = (min_y + max_y) / 2 - center_y
                vertices = [(x, y - shift_y) for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_7:
                # Odwrócenie dziesięciokąta do góry nogami i rozciągnięcie dwukrotnie w pionie dla klawisza 7
                vertices = [(x, 2 * center_y - y) for x, y in reference_vertices]
                vertices = [(x, int(2 * (y - center_y) + center_y)) for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_8:
                # Efekt dla klawisza 8
                scale_factor_x = 2
                scale_factor_y = 1
                angle_rotation = 30  # Obrót w dół o 30 stopni
                translation_y = -50
                translation_x = -250  # Przesunięcie w prawo o 50 pikseli
                
                # Skalowanie
                vertices = [(scale_factor_x * x, scale_factor_y * y) for x, y in reference_vertices]

                # Obrót
                angle_rad = math.radians(angle_rotation)
                vertices = [(int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                            int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                            for x, y in vertices]

                # Translacja w pionie
                vertices = [(x, y + translation_y) for x, y in vertices]

                # Translacja w osi X
                vertices = [(x + translation_x, y) for x, y in vertices]

                display_polygon = True
            elif event.key == pygame.K_9:
         # Efekt dla klawisza 9
                angle_rotation = 180
                shear_factor = 0.3
                translation_x = -165
                
                # Obrót
                angle_rad = math.radians(angle_rotation)
                vertices = [(int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                            int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                            for x, y in reference_vertices]

                # Shear
                vertices = [(x, x * shear_factor + y) for x, y in vertices]

                # Translacja w osi X
                vertices = [(x + translation_x, y) for x, y in vertices]
                
                display_polygon = True











    # Wypełnienie tła
    window.fill(background_color)

    # Rysowanie dziesięciokąta z ciemniejszym środkiem (jeśli zmienna display_polygon jest True)
    if display_polygon:
        pygame.draw.polygon(window, polygon_color, vertices)
        pygame.draw.polygon(window, center_color, vertices, 0)  # Wypełnienie środka
        pygame.draw.polygon(window, border_color, vertices, 2)  # Rysowanie obramówki

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie działania pygame
pygame.quit()
