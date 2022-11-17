from dataclasses import dataclass 


@dataclass
class Params:
        depth: int 
        epochs: int 
        learning_rate: float
        batch_size: int 
        patch_x: int 
        patch_y: int 
        kern_size: int 
        n_patches_per_image: int 
        startfilter: int 
        erosion_iterations: int
        generate_npz: bool 
        validation_split: float 
        n_channel_in: int 
        train_unet: bool 
        train_star: bool 
        train_loss: str
        file_type: str
        min_size: int 
        min_size_mask: int 
        max_size: int 
        n_tiles: tuple
        axes: str
               
    
@dataclass
class Paths: 
    model_dir: str 
    unet_model_dir:  str
    predict_image_dir: str
    save_dir: str 
    base_dir: str
    raw_dir: str
    binary_mask_dir: str
    
@dataclass
class Files:  
    npz_filename: str
    unet_model_name: str
       
    
    
@dataclass
class  VollSegConfig:
    
      paths_vollseg: Paths
      files_vollseg: Files 
      params: Params 
    
        
    


  
