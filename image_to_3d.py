
import cv2
import numpy as np
import open3d as o3d

def image_to_3d(image_path, output_path="output.ply"):
    # Image ko load karo
    print("Image load ho rahi hai...")
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Depth map banao (simple method)
    depth = cv2.GaussianBlur(gray, (5,5), 0)

    # Point cloud banao
    h, w = gray.shape
    points = []
    colors = []

    for y in range(0, h, 2): # 2 pixel skip karenge taaki fast ho
        for x in range(0, w, 2):
            z = depth[y, x] / 10.0  # depth se Z banaya
            points.append([x, y, z])
            colors.append(img[y, x] / 255.0)

    print(f"Total points: {len(points)}")

    # 3D model banao
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors[:, ::-1]) # BGR to RGB

    # Save karo
    o3d.io.write_point_cloud(output_path, pcd)
    print(f"3D model save ho gaya: {output_path}")

# Yahan se run hoga
if __name__ == "__main__":
    image_to_3d("photo.jpg")