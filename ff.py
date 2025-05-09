import os
import time
import math

# 정십이면체의 면을 아스키 아트로 그리기
def draw_dodecahedron(rotation_angle_x, rotation_angle_y):
    # 회전 각도를 라디안으로 변환
    theta_x = math.radians(rotation_angle_x)
    theta_y = math.radians(rotation_angle_y)
    
    # 정십이면체의 3D 좌표 (12개의 면, 20개의 꼭짓점)
    vertices = [
        [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
        [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1],
        [0, 1 / math.sqrt(5), math.sqrt(1 - 1 / math.sqrt(5)**2)],
        [0, -1 / math.sqrt(5), math.sqrt(1 - 1 / math.sqrt(5)**2)],
        [1 / math.sqrt(5), math.sqrt(1 - 1 / math.sqrt(5)**2), 0],
        [-1 / math.sqrt(5), math.sqrt(1 - 1 / math.sqrt(5)**2), 0],
        [0, math.sqrt(1 - 1 / math.sqrt(5)**2), 1]
    ]

    # 회전 행렬 계산 (X축 회전)
    def rotate_x(vertex, angle):
        x, y, z = vertex
        y_new = y * math.cos(angle) - z * math.sin(angle)
        z_new = y * math.sin(angle) + z * math.cos(angle)
        return [x, y_new, z_new]

    # 회전 행렬 계산 (Y축 회전)
    def rotate_y(vertex, angle):
        x, y, z = vertex
        x_new = x * math.cos(angle) + z * math.sin(angle)
        z_new = -x * math.sin(angle) + z * math.cos(angle)
        return [x_new, y, z_new]

    # 정십이면체의 각 점을 회전시키기
    rotated_vertices = []
    for vertex in vertices:
        vertex = rotate_x(vertex, theta_x)
        vertex = rotate_y(vertex, theta_y)
        rotated_vertices.append(vertex)

    # 2D로 투영하기 (z 값 무시)
    projection = []
    for vertex in rotated_vertices:
        x, y, _ = vertex
        projection.append([int(x * 5 + 20), int(y * 5 + 10)])

    # 화면에 정십이면체 그리기
    dodecahedron = [[' ' for _ in range(40)] for _ in range(20)]
    
    # 정십이면체의 면을 그리기 (각 꼭짓점 간의 선분 연결)
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0), # ...
    ]
    
    # 선분 그리기
    for edge in edges:
        start, end = edge
        x1, y1 = projection[start]
        x2, y2 = projection[end]
        
        # 선을 그리기 위해 두 점 사이에 `*` 찍기 (단순한 직선으로 연결)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        
        while True:
            if 0 <= x1 < 40 and 0 <= y1 < 20:
                dodecahedron[y1][x1] = '*'  # 선분 위치에 `*` 찍기

            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    # 정십이면체 출력
    return "\n".join("".join(row) for row in dodecahedron)

# 애니메이션 반복
rotation_angle_x = 0
rotation_angle_y = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # 터미널 화면 지우기
    print(draw_dodecahedron(rotation_angle_x, rotation_angle_y))
    
    # 회전 속도를 더 빠르게 하기 위해 각도 증가값을 5로 설정
    rotation_angle_x += 5  # X축 회전 속도를 더 빠르게
    rotation_angle_y += 5  # Y축 회전 속도를 더 빠르게
    
    # 프레임 간의 시간 간격을 더 줄여서 속도 증가
    time.sleep(0.05)  # 각 프레임 간의 간격을 0.05초로 줄여서 속도 증가

