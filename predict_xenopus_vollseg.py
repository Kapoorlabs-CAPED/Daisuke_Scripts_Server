import os
import glob
from tifffile import imread
from vollseg import StarDist3D, UNET, VollSeg, MASKUNET

import hydra
from config_vollseg import VollSegConfig
from hydra.core.config_store import ConfigStore

configstore = ConfigStore.instance()
configstore.store(name = 'VollSegConfig', node = VollSegConfig)

@hydra.main(config_path = 'conf', config_name = 'config_vollseg')
def main( config : VollSegConfig):

                image_dir = config.paths_vollseg.predict_image_dir
                model_dir = config.paths_vollseg.model_dir
                save_dir = config.paths_vollseg.save_dir
                
                unet_model_name = config.files_vollseg.unet_model_name
                unet_model = UNET(config = None, name = unet_model_name, basedir = model_dir)
                

                Raw_path = os.path.join(image_dir, config.params.file_type)
                filesRaw = glob.glob(Raw_path)
                filesRaw.sort
               
                min_size = config.params.min_size
                min_size_mask = config.params.min_size_mask
                max_size = config.params.max_size
                n_tiles = config.params.n_tiles
                axes = config.params.axes
                
                for fname in filesRaw:
                
                                image = imread(fname)
                                Name = os.path.basename(os.path.splitext(fname)[0])
                                VollSeg( image, 
                                        unet_model = unet_model, 
                                        axes = axes, 
                                        min_size = min_size,  
                                        min_size_mask = min_size_mask,
                                        max_size = max_size,
                                        n_tiles = n_tiles,
                                        save_dir = save_dir, 
                                        Name = Name,
                                        dounet = dounet)   
                                        
if __name__=='__main__':
     main()                                         
